from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Student.models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os
from django.contrib import messages
from django.db.models import Q


# Create your views here.
# running main prouducts page. Getting submission form data and then returning that data to tables 
@login_required(login_url='/login/')
def product(request):

  if request.method == 'POST':
    data = request.POST
    product_name = data.get('product_name')
    product_description = data.get('product_description')
    product_image = request.FILES.get('product_image')

    Product.objects.create(product_name=product_name
                        ,product_description=product_description
                        ,product_image=product_image)
    
## returning back to product page

    return redirect('/product/') 

    
  all_product= Product.objects.all()
  if request.GET.get('search_input'):
    all_product = all_product.filter(product_name__icontains=request.GET.get('search_input'))
  Context={'product':all_product} 
  return render(request,'home/product.html',context=Context)

def employee_view(request):
  if request.method=="POST":
    data = request.POST
    employee_name = data.get('employee_name')
    employee_email = data.get('employee_email')
    employee_address = data.get('employee_address')
    employee_salary = data.get('employee_salary')
    employee_experience = data.get('employee_experience')
    employee_photo = data.get('employee_photo')

    ########## SAVING ABOVE USER DATA TO DB IN BELOW OPERATION  ############
    employee_model = Employee_model.objects.create(name=employee_name,email=employee_email,address=employee_address,
                          salary=employee_salary,experience=employee_experience)
    employee_model.save()
    return redirect('/employee/')#
  employee_all = Employee_model.objects.all() 

  Context={'employee_model':employee_all}
  
  return render(request,'home/employee.html',context=Context) 
    

######delete product button functionality
def delete_product(pk):
      product = Product.objects.get(id=pk)
      product.delete()
      Context={"product":product}
      
      return redirect('/product/',context=Context)


######## update button functionality
def update_product(request,pk):
  pdct =Product.objects.get(id=pk)
  Context = {'update':pdct}
  
  if request.method=='POST':
    data = request.POST

    updated_name = data.get('product_name')
    updated_description = data.get('product_description')
    updated_image = request.FILES.get('product_image')

    

    pdct.product_name = updated_name
    pdct.product_description = updated_description
    pdct.product_image = updated_image
    
    pdct.save()

    return redirect('/product/')

  
  return render(request,'home/update.html',context=Context)


###### search functionality

#def search(request,product_name):
#  if request.method=='POST':
#    data = request.POST
#    search_input = data.get('search_input')
#    if data:
#      results = Product.objects.filter(product_name__icontains=search_input)
#    Context={'results':results}  
#  return redirect('/product/',context=Context)

@login_required(login_url='/login/')
def student_data(request):
  if request.method == 'POST':
    # Handle the form submission
    # You can access the form data using request.POST
    data= request.POST
    student_name = data.get('name')
    student_age = data.get('age')
    student_address = data.get('address')

    ####showing data on terminal that has been sent to server or database.############
    print(student_name)
    print(student_age)
    print(student_address)
    ###############################


    ###Creates a new student record in the database from website form directly.
    Student_model.objects.create(name = student_name,
                                 address =student_address,
                                 age=student_age
                                 )
    ##################################
    
    return redirect('/')
    
    ######### Here you can save the data to the database if needed
  students = [{'name':'Mustafa','roll_no':13,'age':19,'Class':11,'Address':'Shankar'},
              {'name':'Abdullah','roll_no':18,'age':18,'Class':13,'Address':'Chatto'},
              {'name':'Sara','roll_no':41,'age':15,'Class':12,'Address':'Mohib banda'},
              {'name':'Gulalai','roll_no':16,'age':13,'Class':10,'Address':'Peshawar'},
              {'name':'Amina','roll_no':36,'age':15,'Class':9,'Address':'Mardan'},
              {'name':'Jabir','roll_no':26,'age':15,'Class':13,'Address':'Charsadda'},
              {'name':'Zeenat','roll_no':20,'age':12,'Class':12,'Address':'Karachi'},
              {'name':'Saad','roll_no':10,'age':17,'Class':10,'Address':'Lahore'},
              ]
  #################################
  


  return render(request,'home/home.html',{'students':students})

import time


def login_view(request):
  if request.method=='POST':
    data = request.POST

    username = data.get('username')
    user_password = data.get('password')
    user_name = User.objects.filter(username=username)
    if not user_name.exists():
      messages.error(request,'Username does not exist! 🥺')
      return redirect('/login/')

    user = authenticate(username=username,password=user_password)
    if user is None:
      messages.error(request,'Wrong Password 🥺, Try again!')
      return redirect('/login/')
    else:
      login(request,user)
      
      time.sleep(1)
      return redirect('/')
  return render(request,'home/login.html')
      
def logout_view(request):
  logout(request)
  return redirect('/login/')

def register(request):
  
  if request.method=='POST':
    data = request.POST
    username = data.get('user_name')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    user = User.objects.filter(email = email)

    if user.exists():
      messages.error(request,'User with this email already exists!')
      return redirect('/register/')
    
    if data.get('password') == data.get('passwordagain'):
      passwordagain = data.get('passwordagain')
       
    else:
      messages.error(request,'Password do not match!')
      return redirect('/register/')  
   
  
    user = User.objects.create(username=username,first_name=first_name,last_name=last_name,
    email=email,password=password)
    


  return render(request,'home/register.html')

from django.core.paginator import Paginator
def Paginate_Students(request):
  
    
  all_students = Student_model.objects.all()
  if request.GET.get('search'):  ##         It checks if there is a search query parameter in the GET request(GET request means in our template).

    all_students = all_students.filter(Q(name__startswith=request.GET.get('search')) |        #### If there is a search query, 
                                       Q(address__startswith=request.GET.get('search'))|      # it filters the name,address and age. If any of these
                                       Q(age__startswith=request.GET.get('search')))         # are given in search box, it will return those records.
                                                
                                       
                                       
    
    
  paginator = Paginator(all_students, 15)  ###  Creating a paginatroy object with 15 student data per page.
  print(paginator.num_pages)
  data = request.GET
  page_number= data.get('page',1)      ## this code gets the current page number from the GET request. If no page number is specified, it defaults to 1.
  page_object = paginator.get_page(page_number) ##It retrieves the Page object for the specified page number.
  
  
  Context = {'Students':page_object}
  return render(request,'home/paginate_students.html',context=Context)


def See_Student_Marks(request,studentid):
  student = get_object_or_404(Student_model,student_id__studentid=studentid)
  student_marks = Student_marks.objects.filter(student_name=student)
  Context = {'student_marks':student_marks,'student':student}
  return render(request,'home/see_marks.html',context=Context)