from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    Data =Student.objects.all()
    context = {"Data":Data}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name, email, age, gender)
        guery =Student(name=name, email=email, age=age, gender=gender)
        guery.save()
        return redirect("/")
    return render(request, "index.html")

def updateData(request, id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        student = Student.objects.get(id=id)
        student.name = name
        student.email = email
        student.age = age
        student.gender = gender
        student.save()
        return redirect("/")
    
    d = Student.objects.get(id=id)
    context = {"d":d}
    return render(request, "edit.html", context)


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")


