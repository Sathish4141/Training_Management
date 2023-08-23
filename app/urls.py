
from django.urls import path
from . import views

urlpatterns = [
 
    # path('',views.home,name = 'home')
    path('course_create/',views.course_create,name = 'course_create'),
    path('course_deatils_get/',views.course_deatils_get,name = 'course_deatils_get'), #course_deatils_get_one
    path('course_deatils_get_one/<int:cid>',views.course_deatils_get_one,name = 'course_deatils_get_one'), #course_deatils_get_one
    path('course_update/<int:cid>',views.course_update,name = 'course_update'),
    path("course_delete/<int:c_id>",views.course_delete,name = "course_delete"),


    path('student_create/',views.student_create,name = 'student_create'),
    path('student_get/',views.student_get,name = 'student_get'),
    path('student_get_one/<int:sid>',views.student_get_one,name = 'student_get_one'),
    path('update_student/<int:sid>',views.update_student,name = 'update_student'),
    path("delete_student/<int:sid>",views.delete_student,name = "delete_student"),

    path("course_enrolled/<int:cid>/students/",views.course_enrolled,name = "course_enrolled"),






]