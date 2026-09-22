from django.contrib import admin

from core.models import Company, Education, Project, ProjectImage, Skill


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]


admin.site.register(Skill)
admin.site.register(Company)
admin.site.register(Education)
