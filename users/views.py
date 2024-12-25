from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Users,Fakultets
from .serializer import UserGetSerializer, UserPostSerializer, FakultetsSerializer


@csrf_exempt
def bosh_sahifa(request):
    return redirect('/swagger/')


class UserViewSet(ModelViewSet):
    queryset = Users.objects.filter(is_superuser=False)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'role']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return UserGetSerializer
        return UserPostSerializer  # POST, PUT, PATCH uchun


class FakultetsViewSet(ModelViewSet):
    queryset = Fakultets.objects.all()
    serializer_class = FakultetsSerializer