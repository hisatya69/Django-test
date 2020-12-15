from django.shortcuts import render
from .models import Student,Course
# Create your views here.
def ottview(request):
    students=Student.objects.filter(PostalCode__exact=533101)
    return render(request,'ott.html',{'students':students})

