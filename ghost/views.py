
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .forms import dbDetails
import mysql.connector

def index(request):
    context = {}
    context['form'] = dbDetails()
    return render(request, 'ghost/index.html', context)

def ghost_worker(request):
    if request.method == 'POST':
        dbName = request.POST['dbName']
        dbUser = request.POST['dbUser']
        dbPassword = request.POST['dbPassword']

    mydb = mysql.connector.connect(
        host="localhost",
        user=dbUser,
        password=dbPassword,
        database=dbName
    )
