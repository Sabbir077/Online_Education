from django.db import models


# Create your models here.
class Student(models.Model):
    studentName = models.CharField(max_length=50)
    studentAddress = models.CharField(max_length=50)
    studentInstitution = models.CharField(max_length=50)
    studentClass = models.CharField(max_length=10)
    studentContact = models.CharField(max_length=50)
    def __str__(self):
        return self.studentName



class Teacher(models.Model):
    teacherName = models.CharField(max_length=50)
    teacherAddress = models.CharField(max_length=50)
    teacherInstitution = models.CharField(max_length=50)
    teacherDesignation = models.CharField(max_length=50)
    teacherContact = models.CharField(max_length=50)
    def __str__(self):
        return self.teacherName

class Course(models.Model):
    courseTitle = models.CharField(max_length=50)
    courseCatagory = models.CharField(max_length=50)
    startDate = models.CharField(max_length=30)
    courseTeacher = models.ManyToManyField(Teacher)
    courseStudent = models.ManyToManyField(Student)
    def __str__(self):
        return self.courseTitle



class Exam(models.Model):
    examName = models.CharField(max_length=100)
    examComplexity = models.CharField(max_length=20)
    examMarks = models.IntegerField()
    examDuration = models.IntegerField()
    course = models.ForeignKey(Course)
    def __str__(self):
        return self.examName



class MCQ(models.Model):
    question = models.CharField(max_length=500)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    correctAnswer = models.CharField(max_length=100)
    exam =models.ForeignKey(Exam)
    def __str__(self):
        return self.exam.examName + '-' + str(self.id)


