from django.contrib import admin
from .models import Student,Course
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['Name','Roll_no','DateOfJoining','Address','PostalCode']
class CourseAdmin(admin.ModelAdmin):
    list_display = ['s_name','cname','duration','No_of_Subjects']

admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
