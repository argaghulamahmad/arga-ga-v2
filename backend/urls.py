"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import *

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('social', SocialViewSet)
router.register('skill', SkillViewSet)
router.register('interest', InterestViewSet)
router.register('contact', ContactViewSet)
router.register('achievement', AchievementViewSet)
# router.register('activity', ActivityViewSet)
router.register('education', EducationViewSet)
# router.register('project_technology', ProjectTechnologyViewSet)
# router.register('experience_technology', ExperienceTechnologyViewSet)
router.register('project', ProjectViewSet)
router.register('experience', ExperienceViewSet)
router.register('guest', GuestViewSet)
router.register('workflow', WorkflowViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index, name='index'),
    path('experience/', index, name='index'),
    path('education/', index, name='index'),
    path('projects/', index, name='index'),
    path('skills/', index, name='index'),
    path('interests/', index, name='index'),
    path('achievements/', index, name='index'),
    path('contact-me/', index, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
]
