"""Génère une version statique du portfolio dans le dossier _site.

Le site n'a aucune partie dynamique côté visiteur (pas de formulaire, pas de
compte) : la page d'accueil est rendue une fois par Django, puis publiée telle
quelle avec ses fichiers statiques et ses médias, sur GitHub Pages par
exemple. Aucun serveur, aucune mise en veille, aucun quota d'heures.

    python build_static.py            # publié sous /cv (https://<compte>.github.io/cv/)
    SITE_BASE= python build_static.py # publié à la racine d'un domaine
"""

import json
import os
import re
import shutil
import tempfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SITE_BASE = os.environ.get('SITE_BASE', '/cv').rstrip('/')
OUT = BASE_DIR / '_site'

# Mode production du site (DEBUG désactivé) et base de données jetable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
os.environ['RENDER'] = '1'
os.environ['RENDER_EXTERNAL_HOSTNAME'] = 'localhost'
os.environ.setdefault('SECRET_KEY', 'build-statique-sans-secret')

import django  # noqa: E402

django.setup()

from django.conf import settings  # noqa: E402
from django.core.management import call_command  # noqa: E402
from django.db import connection  # noqa: E402
from django.test import Client  # noqa: E402


def main():
    # La base de données du build est reconstruite depuis les migrations
    db_path = Path(settings.DATABASES['default']['NAME'])
    connection.close()
    if db_path.exists():
        db_path.unlink()
    call_command('migrate', verbosity=0)
    call_command('collectstatic', interactive=False, clear=True, verbosity=0)

    response = Client(HTTP_HOST='localhost').get('/', secure=True)
    if response.status_code != 200:
        raise SystemExit(f'La page d\'accueil renvoie {response.status_code}')
    html = response.content.decode('utf-8')

    # Les ressources sont référencées sous /static/ et /media/ : on ajoute le
    # préfixe de publication (le site est servi sous /cv/ sur GitHub Pages).
    html = re.sub(r'(?<=["\'(=,\[\s])/(static|media)/', rf'{SITE_BASE}/\1/', html)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    (OUT / 'index.html').write_text(html, encoding='utf-8')
    (OUT / '.nojekyll').write_text('', encoding='utf-8')

    # Fichiers statiques (sans les copies .gz/.br de WhiteNoise ni l'admin)
    def ignorer(_dossier, noms):
        return [n for n in noms if n.endswith(('.gz', '.br'))]

    shutil.copytree(settings.STATIC_ROOT, OUT / 'static', ignore=ignorer)
    shutil.rmtree(OUT / 'static' / 'admin', ignore_errors=True)

    # Le site ne référence que les noms avec empreinte : on retire la copie au
    # nom simple, sauf pour les vidéos, dont l'adresse directe est utilisée
    # dans les CV (/static/core/videos/<nom>.mp4).
    manifeste = json.loads((settings.STATIC_ROOT / 'staticfiles.json').read_text(encoding='utf-8'))
    for source, avec_empreinte in manifeste['paths'].items():
        if source == avec_empreinte:
            continue
        if source.startswith('core/videos/'):
            # une seule copie (nom simple), la page est réécrite en conséquence
            (OUT / 'static' / avec_empreinte).unlink(missing_ok=True)
            html = html.replace(f'{SITE_BASE}/static/{avec_empreinte}', f'{SITE_BASE}/static/{source}')
        else:
            (OUT / 'static' / source).unlink(missing_ok=True)
    (OUT / 'index.html').write_text(html, encoding='utf-8')
    shutil.copytree(settings.MEDIA_ROOT, OUT / 'media')

    # Vérification : toute ressource locale référencée existe dans _site
    manquantes = []
    for chemin in set(re.findall(rf'["\'(=]({re.escape(SITE_BASE)}/(?:static|media)/[^"\')\s?#]+)', html)):
        if not (OUT / chemin[len(SITE_BASE) + 1:]).exists():
            manquantes.append(chemin)
    if manquantes:
        raise SystemExit('Ressources introuvables : ' + ', '.join(sorted(manquantes)))

    taille = sum(f.stat().st_size for f in OUT.rglob('*') if f.is_file()) / 1e6
    print(f'Site statique généré dans {OUT} ({taille:.1f} Mo), préfixe "{SITE_BASE}"')


if __name__ == '__main__':
    main()
