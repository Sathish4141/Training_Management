from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Course
# Create your views here.

# def home(request):
#     return HttpResponse("HELLO WORLD")

@csrf_exempt
def course_create(request):
    if request.method == 'POST':
        data  = json.loads(request.body)
        course_id = data["course_id"]
        # print(course_id)
        course_name = data["course_name"]
        course_trainer = data["course_trainer"]
        course_timings = data["course_timings"]
        course_fees = data["course_fees"]
        # print(data)
        # print(type(data))
        c = Course(course_id = course_id, course_name = course_name,course_trainer = course_trainer,course_timings = course_timings,course_fees = course_fees)

        c.save()

    #     # return {"data":data}

    return HttpResponse("success fully created course")

def course_deatils_get(request):
    details = Course.objects.all().values()
    print("**************** course details  ************")
    for deatail in details:
        print(deatail["course_name"])

    return JsonResponse({"message":"all data"})


def course_deatils_get_one(request,cid):
    details = Course.objects.all().values()
    # print(list(details))
    for deatail in details:
        if deatail["course_id"] == cid:
            print("**************** course details  ************")
            print(deatail)
     
            
    return HttpResponse(" single course details fetched")

def course_enrolled(request,cid):
    details = Course.objects.all().values()
    students = Student.objects.all().values()
    # print(list(students))
    course_id = ""
    for deatail in details:
        if deatail["course_id"] == cid:
            print("**************** course ID  ************")
            print("Course ID  : ",deatail["course_id"])
            course_id = deatail["course_id"]
     
    student_list = [each["s_name"] for each in list(students) if each["COURSE_id"] == cid]
    print(student_list)
            
    return HttpResponse(f"course id number:{course_id} , enrolled student : {student_list}")





@csrf_exempt
def course_update(request,cid):
    
    update = Course.objects.get(course_id = cid)

    data = json.loads(request.body)
    # update.course_id
    # update.course_name
    # print(update.course_trainer)
    print("BEFORE UPDATE  : ",update.course_fees)
    update.course_fees = data['course_fees']
    print("AFTER UPDATE  : ",update.course_fees)
    update.save()

    return HttpResponse("updated")



@csrf_exempt
def course_delete(request,c_id):

    delete_record = Course.objects.get(course_id = c_id)
    delete_record.delete()
    print(delete_record)

    return HttpResponse("DELETED DATA SUCCESSFULLY")

@csrf_exempt
def student_create(request):
    data = json.loads(request.body)
    # print(data)
    
    s_id = data["s_id"]
    s_name = data["s_name"]
    father_name = data["father_name"]
    mobile_Number = data["mobile_number"]
    email = data["email"]
    print("SELECT COURSE ID WITH RESPECTIVE COURSE")
    # print(data["COURSE"])
    courses = Course.objects.all().values()
    
    # n = 1
    for course in courses:
        print(f"{course['course_id']}  {course['course_name']}")
        # n = n+1
    id = input("ENTER NUMBER WHICH COURSE YOU INTERESTED  : ")
    courses = Course.objects.get(course_id = id)
    print(courses)
    # COURSE = courses.course_name
    # print(COURSE)
    # course_save = Student.objects.create(COURSE = COURSE)
    
    student_details = Student(s_id = s_id,s_name = s_name,father_name = father_name,mobile_Number = mobile_Number,email = email,COURSE = courses)
    student_details.save()
    # course_save = Student.objects.create(COURSE = COURSE),
    # course_save.save()

    return HttpResponse("Student data created successfully")

@csrf_exempt
def student_get(request):
    students_datails =  Student.objects.all().values()
    for student in students_datails:
        print(student)

    return HttpResponse("FETCHED ALL STUDENT DATA SUCCESSFULLY")




@csrf_exempt
def student_get_one(request,sid):
    students_datails = Student.objects.all().values()
    # print(students_datails)
    try:
        for student in students_datails:
            if student['s_id'] == sid:
                print(student)
    except Exception as exp:
        return HttpResponse(f" id not present   : {exp}")

    return HttpResponse("FETCHED STUDENT DATA SUCCESSFULLY")

@csrf_exempt
def update_student(request,sid):
    data = json.loads(request.body)
    student = Student.objects.get(s_id = sid)
    print("BEFORE UODATE DATA  : ",student)
    student.s_name = data["s_name"]
    student.email = data["email"]
    student.save()
    print("AFTER UPDATE  :  ",student)


    return HttpResponse (" student details updated ")


@csrf_exempt
def delete_student(request,sid):
    try:
        deletes = Student.objects.get(s_id = sid).delete()
        print(deletes)
    except Exception as exp:
        return HttpResponse("ID NOT PRESNET")

    return HttpResponse(" DELETED STUDENTS ")
