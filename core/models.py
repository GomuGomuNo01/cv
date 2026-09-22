from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('data', 'Data'),
        ('ia', 'IA & Automatisation'),
        ('dev', 'Développement'),
        ('outils', 'Outils & Données'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon_name = models.CharField(max_length=50, help_text="Nom de l'icône Material Symbols")
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.category})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    index_number = models.CharField(max_length=10, help_text="Ex: 01, 02")
    short_description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(max_length=250, help_text="Liste séparée par des virgules")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_tech_list(self):
        return self.tech_stack.split(',')

    def __str__(self):
        return self.title

class Experience(models.Model):
    """Pour la section 'Au-delà du code' ou un CV plus détaillé"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    status_label = models.CharField(max_length=100, default="OPERATIONAL")

    def __str__(self):
        return self.title
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, help_text="Ex: Abidjan, Luxembourg, Remote")
    logo = models.ImageField(upload_to='companies/', blank=True, null=True)
    website = models.URLField(blank=True)
    
    # Détails du poste
    job_title = models.CharField(max_length=150, help_text="Ex: Administrateur de Bases de Données")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Laissez vide si vous y êtes encore")
    is_current = models.BooleanField(default=False)
    
    # Description des responsabilités (orienté DevOps/Infra)
    description = models.TextField(help_text="Décrivez vos missions principales (ex: Migration Oracle 11g vers PostgreSQL)")

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.job_title} @ {self.name}"


class Education(models.Model):
    school = models.CharField(max_length=150)
    degree = models.CharField(max_length=200, help_text="Ex: Master IA & Big Data")
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='education/', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Laissez vide si en cours")
    is_current = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} @ {self.school}"