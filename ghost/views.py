
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .forms import dbDetails
import mysql.connector
from datetime import datetime, timedelta


def index(request):
    context = {}
    context['form'] = dbDetails()
    return render(request, 'ghost/index.html', context)


def db_connection(request):
    if request.method == 'POST':
        dbName = request.POST['database_name']
        dbUser = request.POST['database_user']
        dbPassword = request.POST['database_password']

        mydb = mysql.connector.connect(
            host="localhost",
            user=dbUser,
            password=dbPassword,
            database=dbName
        )

        return ghost_worker(request, mydb)

    return render(request, 'ghost/index.html')


def ghost_worker(request, connection):
    def hashable(val):
        try:
            hash(val)
            return True
        except TypeError:
            return False

    ghost_workers = []
    with connection.cursor() as cursor:
        # ssconstraints = datetime.now() - timedelta(days=365)
        cursor.execute("""
            SELECT employee.employee_id, employee.emp_name, employee.email, employee.department, employee.position,
            worklog.start_time AS start, attendance.attendance_date AS last_attendance_date
            FROM employee
            LEFT JOIN worklog ON employee.employee_id = worklog.employee_id
            LEFT JOIN attendance ON employee.employee_id = attendance.employee_id
            WHERE worklog.start_time IS NULL
        """)

        data = cursor.fetchall()

        for data in data:

            employee = {
                'id': data[0],
                'name': data[1],
                'email': data[2],
                'department': data[3],
                'position': data[4],
            }

            ghost_workers.append(employee)
            ghost_workers_set = set(frozenset((k, str(v)) for k, v in i.items() if hashable(v))
                                    for i in ghost_workers)

            ghost_workers = [dict(j) for j in ghost_workers_set]

    return render(request, 'ghost/ghost_workers.html', {'ghost_workers': ghost_workers})
