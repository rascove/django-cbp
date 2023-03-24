from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from itreporting.models import Issue
from .serializers import UserSerializer, IssueSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all().order_by('date_submitted')
    serializer_class = IssueSerializer