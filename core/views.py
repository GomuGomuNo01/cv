from django.views.generic import TemplateView
from .models import Project, Skill, Company

class PortfolioView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupération des entreprises (ordre décroissant pour l'affichage)
        companies = Company.objects.all().order_by('-start_date')
        context['companies'] = companies
        context['companies_count'] = companies.count()

        # Années d'expérience : valeur figée pour rester cohérente avec les CV
        # ("deux ans d'expérience" = IT-CENTREX + madameb0nplan). Un calcul
        # automatique depuis la date de début la plus ancienne en base
        # inclurait les stages étudiants antérieurs et gonflerait ce nombre.
        context['years_experience'] = 2

        # On organise les compétences par catégorie pour le template
        projects = Project.objects.filter(is_featured=True).order_by('index_number')
        context['projects'] = projects
        context['projects_count'] = projects.count()
        context['skills_data'] = Skill.objects.filter(category='data').order_by('order')
        context['skills_ia'] = Skill.objects.filter(category='ia').order_by('order')
        context['skills_dev'] = Skill.objects.filter(category='dev').order_by('order')
        context['skills_outils'] = Skill.objects.filter(category='outils').order_by('order')

        # Informations de contact affichées dans le footer
        context['location'] = "Paris, France"
        context['availability'] = "Septembre 2026"

        return context
    
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def execute_command(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        command = data.get('command', '').lower().strip()

        # Simulation de commandes basiques
        responses = {
            "ls": "projets/  competences/  cv_cedric_kouadio.pdf  profil.yaml",
            "whoami": "cedric_kouadio",
            "uptime": "master IA & Big Data, ESGI Paris, rentrée septembre 2026",
            "uname -a": "Data Analyst & Developpeur, Paris, FR",
            "help": "Available commands: ls, whoami, uptime, uname -a, clear, date",
            "date": datetime.now().strftime("%a %b %d %H:%M:%S GMT %Y"),
        }

        result = responses.get(command, f"command not found: {command}")
        return JsonResponse({"output": result})