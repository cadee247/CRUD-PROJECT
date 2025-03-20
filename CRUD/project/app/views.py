from django.shortcuts import render, redirect
from .models import Student
import logging

logger = logging.getLogger(__name__)

# Index view for rendering the homepage
def index(request):
    # Fetch all data from the Student model
    data = Student.objects.all()
    print(data)  # For debugging
    context = {"data": data}
    return render(request, "index.html", context)



# Insert data into the database
def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/")
    return render(request,"index.html")


def updateData(request, id):
    # Fetch all data from the Student model
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        return redirect("/")

    d=Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)

def deleteData(request,id):
    # Fetch all data from the Student model
    d=Student.objects.get(id=id)
    d.delete()
    return redirect("/")

    

       
