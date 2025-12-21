from faker import Faker
from Student.models import *
import random
def fake_db(n=10)->None:
  for _ in range(0,10):
    fake = Faker()
    fakename = fake.name()
    fakemail = fake.email()
    fakeaddress = fake.address()
    fakesalary = random.randint(3000,10000)
    jobs = Employee_job.objects.all()
    index = random.randint(0,len(jobs)-1)
    fakejob = jobs[index]
    job_options = ["1 year","2 years","3 years","4 years","5 years"]
    fakexperience = random.choice(job_options)
    
    Employee_model.objects.create(job=fakejob,name = fakename,email = fakemail,address = fakeaddress,
                          salary = fakesalary, experience = fakexperience)
