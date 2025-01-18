from django.urls import path
from .views import LessonsView, LessonDetails, AssignmentsView, AssignmentDetails, StudentsView, StudentDetails, TeachersView, TeacherDetails, PerformanceView, PerformanceDetails

urlpatterns = [
    path('lessons', LessonsView.as_view(), name="lessons"),
    path('lesson/<int:pk>', LessonDetails.as_view(), name="lesson_view"),
    path('assignments', AssignmentsView.as_view(), name="assignments"),
    path('assignment/<int:pk>', AssignmentDetails.as_view(), name="assignment_view"),

    path('students', StudentsView.as_view(), name="student"),
    path('student/<int:pk>', StudentDetails.as_view(), name="student_view"),
    path('teachers', TeachersView.as_view(), name="teacher"),
    path('teacher/<int:pk>', TeacherDetails.as_view(), name="teacher_view"),

    path('performances', PerformanceView.as_view(), name="performance"),
    path('performance/<int:pk>', PerformanceDetails.as_view(), name="performance_view")
]

