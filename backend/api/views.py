from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import *

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class SocialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows social links to be viewed or edited.
    """
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skill links to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class InterestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows interests to be viewed or edited.
    """
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contact to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows achievement to be viewed or edited.
    """
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activity to be viewed or edited.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class EducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows education to be viewed or edited.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows experience to be viewed or edited.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ProjectTechnologyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project technology to be viewed or edited.
    """
    queryset = ProjectTechnology.objects.all()
    serializer_class = ProjectTechnologySerializer


class ExperienceTechnologyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows experience technology to be viewed or edited.
    """
    queryset = ExperienceTechnology.objects.all()
    serializer_class = ExperienceTechnologySerializer