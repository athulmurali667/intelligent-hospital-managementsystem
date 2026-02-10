from django.db import models

# Create your models here.


class login_table(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)


class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    photo=models.FileField()

class hospital_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    latitude=models.FloatField()
    longitude=models.FloatField()


class department_table(models.Model):
    department=models.CharField(max_length=100)
    details=models.CharField(max_length=100)

class complaint_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)

class doctor_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.DateField()
    gender=models.CharField(max_length=100)
    qualifiction=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    HOSPITAL=models.ForeignKey(hospital_table,on_delete=models.CASCADE)
    DEPARTMENT=models.ForeignKey(department_table, on_delete=models.CASCADE)
    photo=models.FileField()


class schedule_table(models.Model):
    DOCTOR=models.ForeignKey(doctor_table,on_delete=models.CASCADE)
    fromtime=models.TimeField()
    totime=models.TimeField()
    date=models.DateField()

class booking_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    SCHEDULE=models.ForeignKey(schedule_table, on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100)

class prescription_table(models.Model):
    BOOK=models.ForeignKey(booking_table,on_delete=models.CASCADE)
    prescription=models.CharField(max_length=500)
    report=models.CharField(max_length=1000)
    files=models.FileField()

class rating_table(models.Model):
    DOCTOR=models.ForeignKey(doctor_table, on_delete=models.CASCADE)
    USER=models.ForeignKey(user_table, on_delete=models.CASCADE)
    rating=models.FloatField()
    review=models.CharField(max_length=1000)
    date=models.DateField()
