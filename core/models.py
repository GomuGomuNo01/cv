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
    CATEGORY_CHOICES = [
        ('data', 'Data & IA'),
        ('dev', 'Développement'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='data')
    index_number = models.CharField(max_length=10, help_text="Ex: 01, 02")
    short_description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(max_length=250, help_text="Liste séparée par des virgules")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    download_link = models.URLField(blank=True, help_text="Lien de téléchargement direct (ex: rapport .pbix)")
    download_label = models.CharField(max_length=60, blank=True, help_text="Ex: .pbix avec données")
    download_link_alt = models.URLField(blank=True, help_text="Second lien de téléchargement (ex: version portable)")
    download_label_alt = models.CharField(max_length=60, blank=True, help_text="Ex: .zip portable")
    is_featured = models.BooleanField(default=True)
    in_progress = models.BooleanField(default=False, help_text="Projet encore en cours de développement")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_tech_list(self):
        return self.tech_stack.split(',')

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    """Images supplémentaires d'un projet, affichées dans une galerie au clic."""
    project = models.ForeignKey(Project, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image {self.order} de {self.project.title}"


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
    
    # Missions principales, une par ligne (affichées comme liste à puces
    # dans le détail dépliable de l'expérience)
    description = models.TextField(help_text="Une mission par ligne")

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['-start_date']

    def get_task_list(self):
        return [line.strip() for line in self.description.splitlines() if line.strip()]

    def __str__(self):
        return f"{self.job_title} @ {self.name}"


class Certification(models.Model):
    """Certification obtenue en dehors du cursus scolaire (AWS, etc.)."""
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=150, help_text="Ex: Amazon Web Services (AWS)")
    issue_date = models.DateField()
    icon_name = models.CharField(max_length=50, default='workspace_premium', help_text="Nom de l'icône Material Symbols")
    certificate_file = models.FileField(upload_to='certifications/', blank=True, null=True, help_text="Certificat au format PDF (optionnel)")
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Certifications"
        ordering = ['order', '-issue_date']

    def __str__(self):
        return f"{self.title} ({self.issuer})"


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