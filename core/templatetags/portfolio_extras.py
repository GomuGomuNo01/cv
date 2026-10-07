from django import template
from django.templatetags.static import static

register = template.Library()


@register.filter
def asset_url(value):
    """Renvoie l'URL d'une ressource : une URL absolue est rendue telle quelle,
    sinon la valeur est traitée comme un chemin de fichier statique (servi par
    WhiteNoise, qui gère les requêtes partielles nécessaires aux vidéos)."""
    if not value:
        return ''
    if value.startswith(('http://', 'https://', '/')):
        return value
    return static(value)
