from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'home.html')

def colleges(request):
    return render(request, 'colleges.html')

def students(request):
    student_data = Student.objects.all()
    return render(request, 'students.html', {"students": student_data})

def address(request):
    return render(request, 'address.html')