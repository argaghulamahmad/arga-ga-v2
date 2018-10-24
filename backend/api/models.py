from django.contrib.contenttypes.models import ContentType
from django.db import models
from rest_framework import serializers


class Message(models.Model):
    sender_name = models.CharField(max_length=200)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
    level = models.CharField(max_length=10)


class Social(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return '%s %s' % (self.name, self.link)


class Contact(models.Model):
    icon_class = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    def __str__(self):
        return '%s: %s' % (self.icon_class, self.content)


class Interest(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return 'Interest %s' % self.content


class Skill(models.Model):
    name = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.name, self.icon_class)


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return '%s' % self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    school_logo = models.URLField()
    school_url = models.URLField()
    major = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return '%s at %s' % (self.degree, self.school)


class Activity(models.Model):
    content = models.CharField(max_length=200)
    education = models.ForeignKey(Education, default=1, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.content


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project_url = models.URLField()

    def __str__(self):
        return '%s' % self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    company_logo = models.URLField()
    company_url = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return '%s at %s' % (self.title, self.company)


class ProjectTechnology(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, default=1, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name


class ExperienceTechnology(models.Model):
    name = models.CharField(max_length=200)
    experience = models.ForeignKey(Experience, default=1, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class InterestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    # activities = ActivitySerializer()

    class Meta:
        model = Education
        fields = '__all__'


class ProjectTechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectTechnology
        fields = '__all__'


class ExperienceTechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExperienceTechnology
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    # technologies = ProjectTechnologySerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    # technologies = ExperienceTechnologySerializer(many=True)

    class Meta:
        model = Experience
        fields = '__all__'
