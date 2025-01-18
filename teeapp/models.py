from django.db import models

# Create your models here.
class Teacher(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=96)
    email = models.EmailField(max_length=124)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    title = models.CharField(max_length=96)
    topic = models.CharField(max_length=64, default="General")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    link = models.URLField(max_length=1050)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    link = models.URLField(max_length=1050)

    def __str__(self):
        return "for " + self.lesson.title + " by " + self.teacher.name

class Student(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=96)
    email = models.EmailField(max_length=124)
    lesson = models.ManyToManyField(Lesson, null=True)
    assignment = models.ManyToManyField(Assignment, null=True)

    def __str__(self):
        return self.name
    
class Permormance(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    percentage = models.IntegerField()

    def __str__(self):
        return self.student.id

    
