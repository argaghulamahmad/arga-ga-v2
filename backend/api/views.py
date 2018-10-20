from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Message, Social, Skill, MessageSerializer, SocialSerializer, SkillSerializer

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
