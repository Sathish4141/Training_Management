from django.db import models

# Create your models here.


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_trainer = models.CharField(max_length=40)
    course_timings = models.TimeField()
    course_fees = models.FloatField()

    
class Student(models.Model):
    s_id = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mobile_Number = models.BigIntegerField()
    email = models.EmailField(max_length=70) 
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name
    
