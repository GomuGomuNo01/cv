from django.contrib import admin

from core.models import Company, Education, Project, Skill
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Company)
admin.site.register(Education)
# Register your models here.
