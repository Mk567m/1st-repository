from django.db import models 
from Student.models import *
import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.paginator import Paginator

#class Student_model(models.Model):

#  name = models.CharField(max_length=50)
#  age = models.IntegerField()
#  address = models.TextField(blank=True)
#  view_count = models.IntegerField(default=1)
#
#  def __str__(self)-> str:
#    return self.name


# Create your models here.

##############################################
class Department(models.Model):
  department_name=models.CharField(max_length=70)

  def __str__(self)-> str:
    return self.department_name
  class meta:
    ordering = ['department_name']
    verbose_name = 'department_name'


######################
class Student_ID(models.Model):
  studentid = models.CharField(max_length=10,null=True)

  def __str__(self):
    return self.studentid
  class Meta:
    unique_together = ['studentid']
  
#class Date_model(models.Model):
#  date_field = models.DateField(null=True,default="2025",verbose_name="joining date")
  


 
##############################################
class Product(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  product_name = models.CharField(max_length=250)
  product_description = models.TextField(blank=True)
  product_image = models.FileField(upload_to='product/')
  view_count = models.IntegerField(default=1)
  
  def __str__(self) -> str:
    return self.product_name



##############################################
class Student_model(models.Model):
  department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
  student_id = models.OneToOneField(Student_ID,related_name='studentID',on_delete=models.CASCADE,unique=True,null=True)
  name = models.CharField(max_length=50)
  age = models.IntegerField()
  address = models.TextField(blank=True)
  view_count = models.IntegerField(default=1)

  def __str__(self)-> str:
    return self.name    

class Employee_job(models.Model):
  employee_job = models.CharField(max_length=100)
  def __str__(self):
    return self.employee_job



class Employee_model(models.Model):
  job = models.ForeignKey(Employee_job, on_delete=models.CASCADE,null=True)
  name = models.CharField(max_length=100)
  email = models.EmailField()
  address = models.TextField()
  salary = models.DecimalField(decimal_places=2,max_digits=50)
  experience = models.CharField(max_length=40)
  #employee_photo

  def __str__(self):
    return self.name

class Subjects(models.Model):
  subject = models.CharField(max_length=50)

  def __str__(self):
    return self.subject


class Student_marks(models.Model):
  student_name = models.ForeignKey(Student_model,on_delete=models.CASCADE)
  subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
  marks = models.IntegerField()
  
  class Meta:
    unique_together = ['student_name','subject']

  def __str__(self):
    return f"{self.student_name.name}: {self.subject.subject}: {self.marks}"



##############################################
#class ToDoList(models.Model):
#  name = models.CharField(max_length=200)

#  def __str__(self):
#    return self.name



##############################################
#class Item(models.Model):
#  todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
#  text = models.TextField()
#  is_complete = models.BooleanField()True

#  def __str__(self):
#      return self.text  

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  image = models.ImageField(upload_to='profile/',default='default_image.png')
  bio = models.TextField(blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.username} profile "