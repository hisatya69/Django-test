from django.db import models
# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=200)
    Roll_no=models.IntegerField()
    DateOfJoining=models.DateField()
    Address=models.CharField(max_length=200)
    PostalCode=models.IntegerField()

    def __str__(self):
        return self.Name

class Course(models.Model):
    s_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    cname=models.CharField(max_length=20)
    duration=models.DurationField()
    No_of_Subjects=models.IntegerField()

    def __str__(self):
        return self.cname

# Create Django Model for Below.

# IN collage we have students, courses, I just want to design models for students and Courses.
# Stundents will have below Properties.
# Name, RollNumber, DateOfJoining, Address, Country, PostalCode
# Course will have below Properties.
# Name, duration, NumberOfSubsjects

# write models for Student, Course, and Student Course Releation.

# ORM Queries.

# Retrive all Student from database

# Retrive Students from Country is IN


# Retrive Students whos name contains Sing
# Retrive Students whose postal code starts with 5000


# we Developed one web site. That web site has more traffic, then  are getting some random requests to few ip addresses.
# we just want to block this requests from specific ip address.
# IP addresses are available in DB, you can query and compre and reject requests.
# what is your approch for this?


# Rest Framework Standards?


# We are implementing few API's which are server for Known Users.
# How can you implement Authentication and Authorization part?
