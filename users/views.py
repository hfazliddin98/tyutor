from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet


@csrf_exempt
def bosh_sahifa(request):
    return redirect('/swagger/')