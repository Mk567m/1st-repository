# BISMILLAH-HI-Rahmani-Raheem
from django.db import IntegrityError
from Student.models import *
import random
from faker import Faker
fake = Faker()
def fake_names(n=5)-> None:
  for _ in range(n):
                                              ################### CREATING STUDENT_MODEL DATA  #######################
    department = Department.objects.all()
    randomindex = random.randint(0,len(department)-1)
    
    fakedepartment = department[randomindex]
    
    
    fake_id = f'ID-{random.randint(1,99999999999999999999999)}'
    fakename = fake.name()
    fakeage = random.randint(15,30)
    fakeaddress = fake.address()
    fakecount = random.randint(1,999999999999)
    randomid = Student_ID.objects.create(studentid=fake_id)

    Student_model.objects.create(department=fakedepartment,student_id = randomid,name=fakename,
                                 age=fakeage,
                                 address=fakeaddress,
                                 view_count=fakecount)
                                 
    
    

def fakemarks(n=10)-> None:
   try:
      all_student = Student_model.objects.all()
      all_subject = Subjects.objects.all()
      for std in all_student:
        for subject in all_subject:
          Student_marks.objects.create(student_name=std,subject=subject,marks=random.randint(0,100))

   except IntegrityError:
       pass

