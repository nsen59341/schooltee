from django.shortcuts import render
from .serializer import LessonSerializer, AssignmentSerializer, StudentSerializer, TeacherSerializer, PerformanceSerializer
from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Teacher, Lesson, Assignment, Student, Permormance

# Create your views here.

class LessonsView(APIView):
    def get(self, request):
        params = request.GET
        if params and params['studId']:
            student = Student.objects.get(id=params['studId'])
            lessons = student.lesson
        else:
            lessons = Lesson.objects.all()
        lessonsSer = LessonSerializer(lessons, many=True)
        return Response(lessonsSer.data, status=status.HTTP_200_OK)
    def post(self, request):
        lesson = request.data
        lessonsSer = LessonSerializer(data=lesson)
        if lessonsSer.is_valid():
            lessonsSer.save()
            return Response(lessonsSer.data, status=status.HTTP_201_CREATED)
        return Response(lessonsSer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

# class AssignmentsView(generics.ListCreateAPIView):
#     queryset = Assignment.objects.all()
#     serializer_class = AssignmentSerializer

class AssignmentsView(APIView):
    def get(self, request):
        params = request.GET
        if params and params['studId']:
            student = Student.objects.get(id=params['studId'])
            assignment = student.assignment
        else:
            assignment = Assignment.objects.all()
        assignmentSer = AssignmentSerializer(assignment, many=True)
        return Response(assignmentSer.data, status=status.HTTP_200_OK)
    def post(self, request):
        assignment = request.data
        assignmentSer = LessonSerializer(data=assignment)
        if assignmentSer.is_valid():
            assignmentSer.save()
            return Response(assignmentSer.data, status=status.HTTP_201_CREATED)
        return Response(assignmentSer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class StudentsView(APIView):
    def get(self, request):
        params = request.GET
        if params and params['email']:
            student = Student.objects.filter(email=params['email']).first()  
            studSer = StudentSerializer(student) 
        else:
            student = Student.objects.all()
            studSer = StudentSerializer(student, many=True) 
        
        print('studSer', studSer.data)
        return Response(studSer.data, status=status.HTTP_200_OK)
    def post(self, request):
        student = request.data
        print('student',student)
        studSer = StudentSerializer(data=student)
        if studSer.is_valid():
            studSer.save()
            return Response(studSer.data, status=status.HTTP_201_CREATED)
        return Response(studSer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeachersView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class PerformanceView(APIView):
    def get(self, request):
        params = request.GET
        if params['student_id'] and params['assignment_id']:
            performances = Permormance.objects.filter(student=params['student_id'], assignment=params['assignment_id']).first()
        elif params['student_id']:
            performances = Permormance.objects.filter(student=params['student_id']).first()
        elif params['assignment_id']:
            performances = Permormance.objects.filter(assignment=params['assignment_id']).first()
        else:
            performances = Permormance.objects.all()
        performanceSer = PerformanceSerializer(performances)
        return Response(performanceSer.data, status=status.HTTP_200_OK)
    def post(self, request):
        performanceSer = PerformanceSerializer(data=request.data)
        if performanceSer.is_valid():
            performanceSer.save()
            return Response(performanceSer.data, status=status.HTTP_201_CREATED)
        return Response(performanceSer.errors, status=status.HTTP_400_BAD_REQUEST)

class PerformanceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permormance.objects.all()
    serializer_class = PerformanceSerializer