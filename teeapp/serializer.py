from .models import Teacher, Lesson, Assignment, Student, Permormance
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class LessonSerializer(serializers.ModelSerializer):

    teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all()
    )  # Use ID for creating/updating lessons
    
    teacher_details = TeacherSerializer(source='teacher', read_only=True)  # Use a nested serializer for output

    class Meta:
        model = Lesson
        fields = "__all__"

    # return teacher name as teacher in api response
    # def get_teacher(self, obj):
    #     return obj.teacher.name if obj.teacher else None  # Get the teacher's name or None if there's no teacher


class AssignmentSerializer(serializers.ModelSerializer):

    teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all()
    )  # Use ID for creating/updating lessons
    
    teacher_details = TeacherSerializer(source='teacher', read_only=True)  # Use a nested serializer for output

    lesson = serializers.PrimaryKeyRelatedField(
        queryset=Lesson.objects.all()
    )  # Use ID for creating/updating lessons
    
    lesson_details = LessonSerializer(source='lesson', read_only=True)  # Use a nested serializer for output

    class Meta:
        model = Assignment
        fields = "__all__"

    # # return teacher name as teacher in api response
    # def get_teacher(self, obj):
    #     return obj.teacher.name if obj.teacher else None  # Get the teacher's name or None if there's no teacher
    
    # # return lesson name as lesson in api response
    # def get_lesson(self, obj):
    #     return obj.lesson.title if obj.lesson else None

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class PerformanceSerializer(serializers.ModelSerializer):

    student = serializers.PrimaryKeyRelatedField(
        queryset = Student.objects.all()
    )
    student_details = StudentSerializer(source="student", read_only=True)

    assignment = serializers.PrimaryKeyRelatedField(
        queryset = Assignment.objects.all()
    )
    assignment_details = AssignmentSerializer(source="assignment", read_only=True)

    class Meta:
        model = Permormance
        fields = "__all__"