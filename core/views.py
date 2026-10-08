from django.views.generic import TemplateView
from .models import Project, Skill, Company, Education, Certification

class PortfolioView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        companies = Company.objects.all().order_by('-start_date')
        context['companies'] = companies
        context['companies_count'] = companies.count()

        educations = Education.objects.all().order_by('-start_date')
        context['educations'] = educations
        context['educations_count'] = educations.count()

        context['certifications'] = Certification.objects.all()

        # Années d'expérience : valeur figée pour rester cohérente avec les CV
        # ("deux ans d'expérience" = IT-CENTREX + madameb0nplan). Un calcul
        # automatique depuis la date de début la plus ancienne en base
        # inclurait les stages étudiants antérieurs et gonflerait ce nombre.
        context['years_experience'] = 2

        # On organise les compétences par catégorie pour le template
        projects = Project.objects.filter(is_featured=True).order_by('index_number').prefetch_related('gallery_images')
        context['projects'] = projects
        context['projects_count'] = projects.count()
        context['projects_data'] = projects.filter(category='data')
        context['projects_dev'] = projects.filter(category='dev')
        # Bandeau défilant sous le hero : version courte des compétences
        # (section Compétences, migration 0052). À garder alignés.
        context['marquee_skills'] = [
            'Python', 'SQL / DuckDB', 'Power BI / DAX', 'PySpark',
            'scikit-learn / XGBoost', 'RAG / LangChain', 'Claude Code / MCP',
            'Playwright', 'FastAPI', 'Java / Spring Boot', 'Laravel',
            'React / TypeScript', 'Docker', 'GitHub Actions',
        ]
        context['skills_data'] = Skill.objects.filter(category='data').order_by('order')
        context['skills_ia'] = Skill.objects.filter(category='ia').order_by('order')
        context['skills_dev'] = Skill.objects.filter(category='dev').order_by('order')
        context['skills_outils'] = Skill.objects.filter(category='outils').order_by('order')

        # Informations de contact affichées dans le footer
        context['location'] = "Paris, France"
        context['availability'] = "Septembre 2026"

        return context