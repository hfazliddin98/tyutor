from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import AccessToken
from datetime import datetime, timezone, timedelta
from rest_framework.viewsets import ModelViewSet
from .models import Users,Fakultets
from .serializers import UserGetSerializer, UserPostSerializer, FakultetsSerializer


@csrf_exempt
def bosh_sahifa(request):
    return redirect('/swagger/')

    
@csrf_exempt
def token_vaqt(request, token):
    try:
        decoded_token = AccessToken(token)
        exp_time_utc = datetime.fromtimestamp(decoded_token['exp'], timezone.utc)
        exp_time_uz = exp_time_utc + timedelta(hours=5)
        return HttpResponse(exp_time_uz)
    except Exception:
        return HttpResponse("Noto‘g‘ri yoki eskirgan token") 


class UserViewSet(ModelViewSet):
    queryset = Users.objects.filter(is_superuser=False)
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'role', 'fakultet']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return UserGetSerializer
        return UserPostSerializer  # POST, PUT, PATCH uchun


class FakultetsViewSet(ModelViewSet):
    queryset = Fakultets.objects.all()
    serializer_class = FakultetsSerializer
    http_method_names = ['get', 'post', 'patch']