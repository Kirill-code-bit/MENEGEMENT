from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Schedule(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title


class AboutPage(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
        
class ContactPage(models.Model):
    address = models.TextField()
    contact_num = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.address


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, default="Male")
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.IntegerField(default=1234567)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50)
    stu_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    grade = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.grade}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.name} - {self.date} - {'Present' if self.is_present else 'Absent'}"

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    isPublic = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.CharField(max_length=20)
    qualification = models.TextField()

    def __str__(self):
        return self.full_name
    
