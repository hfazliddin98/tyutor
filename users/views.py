from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from .models import Users,Fakultets
from .serializer import UserSerializer, FakultetsSerializer


@csrf_exempt
def bosh_sahifa(request):
    return redirect('/swagger/')

class UserViewSet(ModelViewSet):
    queryset = Users.objects.filter(is_superuser=False)
    serializer_class = UserSerializer


class FakultetsViewSet(ModelViewSet):
    queryset = Fakultets.objects.all()
    serializer_class = FakultetsSerializer