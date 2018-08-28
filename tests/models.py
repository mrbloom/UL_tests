from django.db import models
from django.core.validators import MaxValueValidator

from phonenumber_field.modelfields import PhoneNumberField

class CommonInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField(blank=True)

class Teacher(CommonInfo):
    subject = models.CharField(max_length=50)

class Student(CommonInfo):
    avg_mark = models.PositiveSmallIntegerField(validators=[MaxValueValidator])

class Class(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)



class Image(models.Model):
    image = models.ImageField()
    alt_text = models.CharField(max_length=100)

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Question(models.Model):
    title = models.CharField(max_length=100)
    question_text = models.TextField()
    question_answer = models.TextField()
    image = models.ManyToManyField(Image)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)

class Choice(models.Model):
    text = models.TextField()
    image = models.ManyToManyField(Image)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)




