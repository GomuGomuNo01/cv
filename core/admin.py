from django.contrib import admin

from core.models import Company, Project, Skill
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Company)    
# Register your models here.
