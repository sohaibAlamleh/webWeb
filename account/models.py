from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class dumy(models.Model):
     ID = models.AutoField(primary_key=True)
     FirstName = models.CharField(max_length=50)
     LastName = models.CharField(max_length=50)


class User_history(models.Model):
    Search_ID = models.AutoField(primary_key=True)
    Search_query = models.CharField(max_length=50)
    search_result = models.CharField(max_length=50)
    search_date= models.DateField(auto_now_add=True)
    user_ID=models.ForeignKey(User, on_delete=models.CASCADE)




