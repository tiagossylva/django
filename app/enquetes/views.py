from django.shortcuts import render
from django.http import HttpResponse

def index(resquest):
    return HttpResponse("Ola mundo. Você está no índice de enquetes.")
