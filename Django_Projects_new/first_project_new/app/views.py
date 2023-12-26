from django.shortcuts import render, HttpResponse
from .models import Employee

# Create your views here.


def homepage(request):
    emps = Employee.objects.all()
    return render(request, "home.html", context ={"name":["A","B","C","D"], "all_emp":emps})