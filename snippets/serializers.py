from django.contrib.auth.models import User
from rest_framework import serializers
from itreporting.models import Issue

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class IssueSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Issue
        fields = ['type', 'room', 'details', 'date_submitted', 'author']