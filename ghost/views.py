
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .forms import dbDetails
import mysql.connector


def index(request):
    context = {}
    context['form'] = dbDetails()
    return render(request, 'ghost/index.html', context)


def connection_(request):
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
    return mydb


def ghost_worker(request):
    mydb = connection_()
    ghost_workers = []
    with mydb.cursor() as cursor:
        cursor.execute("""
            SELECT e.* w.employee_id, w.task, w.duration, w,status, w.comments
            FROM employee e
            LEFT JOIN worklog w ON e.employee_id = w.employee_id
        """)

        data = cursor.fetchall()

        for data in data:
            if (not data[5] or not data[6] or not data[7] or not data[7]) or (7):
                employee = {
                    'id': data[0],
                    'name': data[1],
                    'email': data[2],
                    'department': data[3],
                    'position': data[4],
                }

                ghost_workers.append(employee)

    return render(request, 'ghost_workers.html', {'ghost_workers': ghost_workers})
