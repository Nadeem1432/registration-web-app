from django.db import models
from django.db.models.fields import EmailField, TextField

# # Create your models here.
# class Table(models.Model):
#     name = models.CharField(max_length=50  ),
#     email = models.EmailField( ),
#     phone = models.CharField(max_length=15),
#     date  = models.DateTimeField( )


class Table(models.Model):
    name         = models.CharField(max_length=150)  # blog name
    phone    	 = models.CharField(max_length=50)
    email		 = models.CharField(max_length=50)
    date	     = models.DateField()

    def __str__(self):
         return  self.name+ ' ... '
