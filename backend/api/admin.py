from django.contrib import admin
from .models import Message, Social, Skill, Activity, ProjectTechnology, ExperienceTechnology, Experience, Project, Achievement, Education, Interest, Contact

# Register your models here.
admin.site.register(Message)
admin.site.register(Social)
admin.site.register(Skill)
admin.site.register(Achievement)
admin.site.register(Activity)
admin.site.register(ProjectTechnology)
admin.site.register(ExperienceTechnology)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Interest)
admin.site.register(Contact)
