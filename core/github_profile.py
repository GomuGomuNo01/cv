"""Données du profil GitHub affichées dans la carte du hero.

Sources publiques, sans authentification :
  - API REST GitHub : profil (/users/<login>) et dépôts (/users/<login>/repos) ;
  - calendrier public des contributions (/users/<login>/contributions).

Les données sont mises en cache 6 h. En cas d'échec (réseau, limite de
requêtes, changement de format), la dernière version valide est réutilisée,
puis à défaut la copie de secours livrée avec le site
(core/data/github_snapshot.json) : la page ne dépend jamais de la
disponibilité de GitHub au moment de l'affichage.
"""

import json
import logging
import os
import re
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone
from pathlib import Path

from django.core.cache import cache

logger = logging.getLogger(__name__)

LOGIN = 'GomuGomuNo01'
CACHE_KEY = 'github_profile'
LAST_GOOD_KEY = 'github_profile_last_good'
CACHE_SECONDS = 6 * 3600
TIMEOUT = 4
WEEKS_SHOWN = 26
SNAPSHOT_PATH = Path(__file__).resolve().parent / 'data' / 'github_snapshot.json'

# Dépôts non montrés dans "dernière activité" : README de profil et dépôt du
# portfolio lui-même (le visiteur est déjà dessus).
HIDDEN_REPOS = {LOGIN.lower(), 'cv'}

# Balisage et outillage ignorés dans la répartition des langages : ils
# apparaissent dans presque tous les dépôts sans refléter le travail réel
# (ex. une page HTML de présentation dans un projet Power BI).
IGNORED_LANGUAGES = {
    'HTML', 'CSS', 'SCSS', 'Dockerfile', 'Shell', 'PowerShell', 'Batchfile',
    'Makefile', 'Procfile', 'Inno Setup', 'Roff',
}

LANGUAGE_COLORS = {
    'Python': '#3572A5', 'JavaScript': '#f1e05a', 'TypeScript': '#3178c6',
    'Java': '#b07219', 'C#': '#178600', 'PHP': '#4F5D95', 'Blade': '#f7523f',
    'Dart': '#00B4AB', 'HTML': '#e34c26', 'CSS': '#563d7c',
    'Jupyter Notebook': '#DA5B0B', 'Go': '#00ADD8', 'Shell': '#89e051',
}


def _get(url, accept='application/vnd.github+json'):
    headers = {'User-Agent': 'cedric-kouadio-portfolio', 'Accept': accept}
    token = os.environ.get('GITHUB_TOKEN')
    if token and 'api.github.com' in url:
        headers['Authorization'] = f'Bearer {token}'
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        return response.read().decode('utf-8')


def _parse_contributions(html):
    """Renvoie [(date, niveau 0-4, nombre)] trié par date."""
    cells = {}
    for td in re.finditer(r'<td\b[^>]*ContributionCalendar-day[^>]*>', html):
        tag = td.group(0)
        day = re.search(r'data-date="(\d{4}-\d\d-\d\d)"', tag)
        level = re.search(r'data-level="(\d)"', tag)
        cell_id = re.search(r'\bid="([^"]+)"', tag)
        if day and level and cell_id:
            cells[cell_id.group(1)] = (day.group(1), int(level.group(1)))
    counts = {}
    for tip in re.finditer(r'<tool-tip\b[^>]*\bfor="([^"]+)"[^>]*>([^<]*)</tool-tip>', html):
        number = re.match(r'\s*(\d+)', tip.group(2))
        counts[tip.group(1)] = int(number.group(1)) if number else 0
    days = [(d, lvl, counts.get(cid, 0)) for cid, (d, lvl) in cells.items()]
    days.sort()
    if len(days) < 300:
        raise ValueError('calendrier des contributions illisible')
    return days


def _time_ago(iso):
    pushed = datetime.fromisoformat(iso.replace('Z', '+00:00'))
    days = (datetime.now(timezone.utc) - pushed).days
    if days <= 0:
        return "aujourd'hui"
    if days == 1:
        return 'hier'
    if days < 14:
        return f'il y a {days} j'
    if days < 60:
        return f'il y a {days // 7} sem.'
    return f'il y a {days // 30} mois'


def _build(user, repos, repo_languages, days):
    own = [r for r in repos if not r.get('fork')]

    # Nombre de dépôts dans lesquels chaque langage est utilisé
    presence = Counter()
    for langs in repo_languages:
        presence.update(k for k in langs if k not in IGNORED_LANGUAGES)
    top = presence.most_common(5)
    max_count = top[0][1] if top else 1
    languages = [
        {'name': name, 'repos': n, 'percent': round(100 * n / max_count),
         'color': LANGUAGE_COLORS.get(name, '#8b949e')}
        for name, n in top
    ]

    def main_language(repo):
        lang = repo.get('language') or ''
        return '' if lang in IGNORED_LANGUAGES else lang

    recent = [
        {'name': r['name'], 'language': main_language(r), 'pushed_at': r['pushed_at'],
         'color': LANGUAGE_COLORS.get(main_language(r), '#8b949e')}
        for r in sorted(own, key=lambda r: r['pushed_at'], reverse=True)
        if r['name'].lower() not in HIDDEN_REPOS
    ][:3]

    # Série en cours : jours consécutifs avec contribution jusqu'à aujourd'hui
    # (aujourd'hui sans contribution ne casse pas la série : la journée
    # n'est pas finie).
    counts = [n for _, _, n in days]
    if counts and counts[-1] == 0:
        counts = counts[:-1]
    current = 0
    for n in reversed(counts):
        if not n:
            break
        current += 1
    best = run = 0
    for _, _, n in days:
        run = run + 1 if n else 0
        best = max(best, run)

    return {
        'login': user['login'],
        'name': user.get('name') or user['login'],
        'avatar_url': user['avatar_url'],
        'html_url': user['html_url'],
        'location': (user.get('location') or '').split(',')[0],
        'member_since': user['created_at'][:4],
        'public_repos': user.get('public_repos', len(own)),
        'followers': user.get('followers', 0),
        'total_contributions': sum(n for _, _, n in days),
        'active_days': sum(1 for _, _, n in days if n),
        'current_streak': current,
        'best_streak': best,
        'days': [[d, lvl, n] for d, lvl, n in days],
        'languages': languages,
        'recent': recent,
        'fetched_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    }


def fetch_github_profile():
    user = json.loads(_get(f'https://api.github.com/users/{LOGIN}'))
    repos = json.loads(_get(f'https://api.github.com/users/{LOGIN}/repos?per_page=100&sort=pushed'))
    own = [r for r in repos if not r.get('fork')]
    with ThreadPoolExecutor(max_workers=8) as pool:
        repo_languages = list(pool.map(lambda r: json.loads(_get(r['languages_url'])), own))
    days = _parse_contributions(_get(f'https://github.com/users/{LOGIN}/contributions', accept='text/html'))
    return _build(user, repos, repo_languages, days)


MONTHS = ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin',
          'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.']


def _weeks(days):
    """Dernières semaines du calendrier, en colonnes de 7 jours (dimanche en
    haut), et libellés des mois positionnés sur la colonne où ils commencent."""
    by_date = {d: (lvl, n) for d, lvl, n in days}
    last = date.fromisoformat(days[-1][0])
    start = last.toordinal() - (last.isoweekday() % 7) - 7 * (WEEKS_SHOWN - 1)
    weeks, months = [], []
    for w in range(WEEKS_SHOWN):
        column = []
        for d in range(7):
            day = date.fromordinal(start + 7 * w + d)
            lvl, n = by_date.get(day.isoformat(), (None, 0))
            label = f"{n} contribution{'s' if n > 1 else ''} le {day.day} {MONTHS[day.month - 1]}"
            column.append({'level': lvl, 'label': label})
        weeks.append(column)
        first = date.fromordinal(start + 7 * w)
        if w == 0 or first.day <= 7:
            months.append({'column': w + 1, 'name': MONTHS[first.month - 1]})
    # évite deux libellés collés en tout début de grille
    if len(months) > 1 and months[1]['column'] - months[0]['column'] < 3:
        months.pop(0)
    return weeks, months


def _decorate(data):
    """Ajoute les champs calculés à l'affichage (relatifs à aujourd'hui)."""
    data = dict(data)
    data['weeks'], data['months'] = _weeks(data['days'])
    data['recent'] = [dict(r, ago=_time_ago(r['pushed_at'])) for r in data['recent']]
    total = sum(l['repos'] for l in data['languages']) or 1
    data['languages'] = [dict(l, share=round(100 * l['repos'] / total, 1)) for l in data['languages']]
    return data


def get_github_profile():
    data = cache.get(CACHE_KEY)
    if data is None:
        try:
            data = fetch_github_profile()
            cache.set(LAST_GOOD_KEY, data, None)
        except Exception as exc:  # réseau, limite de requêtes, format modifié
            logger.warning('Profil GitHub indisponible, données de secours utilisées : %s', exc)
            data = cache.get(LAST_GOOD_KEY)
            if data is None:
                try:
                    data = json.loads(SNAPSHOT_PATH.read_text(encoding='utf-8'))
                except (OSError, ValueError):
                    return None
        cache.set(CACHE_KEY, data, CACHE_SECONDS)
    return _decorate(data)
