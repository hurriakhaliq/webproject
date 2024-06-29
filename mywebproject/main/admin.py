from django.contrib import admin
from .models import Education, Experience, Skill, Project, ContactForm, OwnerDetails


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'project_url']


admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(ContactForm)
admin.site.register(OwnerDetails)