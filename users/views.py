from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import AccessToken
from datetime import datetime, timezone, timedelta
from rest_framework.viewsets import ModelViewSet
from users.models import Users,Fakultet, Yonalish, Kurs, Guruh, Talaba
from users.serializers import UserGetSerializer, UserPostSerializer
from users.serializers import FakultetGetSerializer, FakultetPostSerializer, YonalishGetSerializer, YonalishPostSerializer
from users.serializers import KursGetSerializer, KursPostSerializer, GuruhGetSerializer, GuruhPostSerializer
from users.serializers import TalabaGetSerializer, TalabaPostSerializer


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
    # queryset = Users.objects.filter(is_superuser=False)
    http_method_names = ['get', 'post', 'patch']
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = [
        'username', 'role', 'fakultet'
    ]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return UserGetSerializer
        return UserPostSerializer  # POST, PUT, PATCH uchun
    
    def get_queryset(self):
        queryset = Users.objects.prefetch_related('guruh').filter(is_superuser=False)
        fakultet_id = self.request.query_params.get('fakultet', None)

        if fakultet_id:
            queryset = queryset.filter(fakultet_id=fakultet_id)

        return queryset
    
# class UserViewSet(ModelViewSet):
#     queryset = Users.objects.filter(is_superuser=False)
#     http_method_names = ['get', 'post', 'patch']
#     filter_backends = [DjangoFilterBackend,]
#     filterset_fields = [
#         'username', 'role', 'fakultet'
#     ]

#     def get_serializer_class(self):
#         if self.action in ['list', 'retrieve']:  # GET uchun
#             return UserGetSerializer
#         return UserPostSerializer  # POST, PUT, PATCH uchun


class FakultetViewSet(ModelViewSet):
    queryset = Fakultet.objects.all()
    http_method_names = ['get', 'post', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'id',
        'yonalishlar__id',
        'yonalishlar__kurslar__id',
        'yonalishlar__kurslar__guruhlar__id',
        ]
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return FakultetGetSerializer
        return FakultetPostSerializer  # POST, PUT, PATCH uchun


class YonalishViewSet(ModelViewSet):
    queryset = Yonalish.objects.all()
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return YonalishGetSerializer
        return YonalishPostSerializer  # POST, PUT, PATCH uchun

class KursViewSet(ModelViewSet):
    queryset = Kurs.objects.all()
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return KursGetSerializer
        return KursPostSerializer  # POST, PUT, PATCH uchun

class GuruhViewSet(ModelViewSet):
    queryset = Guruh.objects.all()
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return GuruhGetSerializer
        return GuruhPostSerializer  # POST, PUT, PATCH uchun

class TalabaViewSet(ModelViewSet):
    queryset = Talaba.objects.all()
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return TalabaGetSerializer
        return TalabaPostSerializer  # POST, PUT, PATCH uchun