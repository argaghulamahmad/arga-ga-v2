from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class Social(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return '%s %s' % (self.name, self.link)


class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Social
        fields = ('url', 'name', 'link', 'pk')


class Skill(models.Model):
    name = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.name, self.icon_class)


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ('url', 'name', 'icon_class', 'pk')
