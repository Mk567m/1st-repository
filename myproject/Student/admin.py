from django.contrib import admin
from Student.models import *
# Register your models here.

class display_student_view(admin.ModelAdmin):
  list_display = ['name','department','age']
admin.site.register(Student_model,display_student_view)
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Student_ID)
admin.site.register(Employee_job)
admin.site.register(Employee_model)
admin.site.register(Profile)
admin.site.register(Subjects)
class display_student_record(admin.ModelAdmin):
  list_display = ['student_name','subject','marks']

admin.site.register(Student_marks,display_student_record)