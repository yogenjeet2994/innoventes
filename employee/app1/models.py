from django.db import models

# Create your models here.

class Company(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    company_name = models.CharField(max_length=5)
    email_id = models.EmailField()
    company_code = models.CharField(max_length=5, unique=True, )
    strength = models.IntegerField()
    website = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.company_name


