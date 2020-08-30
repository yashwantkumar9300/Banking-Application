from django.db import models

class Admin(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default=True)
    contact = models.IntegerField(default=True)
    email = models.CharField(max_length=50,default=True)
    uname = models.CharField(max_length=50,default=True)
    password = models.CharField(max_length=50,default=True)
    address = models.CharField(default=True,max_length=100)

class SavingAccount(models.Model):
    acno = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50,default=True)
    lname = models.CharField(max_length=50,default=True)
    ftname = models.CharField(max_length=50,default=True)
    mname = models.CharField(max_length=50,default=True)
    dob = models.DateField(default=True)
    gender = models.CharField(max_length=20,default=True)
    adhar = models.IntegerField(unique=True,default=True)
    national = models.CharField(max_length=50,default=True)
    mobile = models.IntegerField(unique=True,default=True)
    email = models.CharField(unique=True,max_length=50,default=True)
    photo = models.ImageField(upload_to='images/',default=True)
    sign = models.ImageField(upload_to='images/',default=True)
    balance = models.FloatField(default='0.0')
    password = models.CharField(max_length=20, default=True)
    status = models.CharField(max_length=20, default='Active')
    house = models.CharField(max_length=20,default=True)
    street = models.CharField(max_length=50,default=True)
    village = models.CharField(max_length=50,default=True)
    city = models.CharField(max_length=50,default=True)
    post = models.CharField(max_length=50,default=True)
    pin = models.IntegerField(default=True)
    state = models.CharField(max_length=50,default=True)
    dist = models.CharField(default=True,max_length=50)

class Statement(models.Model):
    acno = models.IntegerField(default=True)
    date = models.DateField(auto_now_add=True)
    reference = models.IntegerField(default=True)
    particular = models.CharField(max_length=50,default=True)
    credit = models.FloatField(default=0.0)
    debit = models.FloatField(default=0.0)
    balance = models.FloatField(default=True)






