from django.db import models

# Create your models here.
class Dam(models.Model):
    categories = (
        ('small', 'small'),
        ('Medium', 'Medium'),
        ('Large', 'Large')

    )
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to="Image/",blank=True)
    no_fishes = models.IntegerField()
    category = models.CharField(max_length=50, choices=categories)
    location = models.TextField(max_length=200,null=True)
    about = models.CharField(max_length=200,null=True)


class New_department(models.Model):
    dep_name = models.TextField(max_length=200,blank=True)
    dep_discription = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.dep_name

class Staff(models.Model):
    first_name = models.TextField(max_length=200,blank=True)
    last_name = models.TextField(max_length=200,blank=True)
    salary = models.IntegerField(blank=True)
    mobile = models.IntegerField(blank=True)
    state = models.TextField(max_length=200,blank=True)
    country = models.TextField(max_length=200,blank=True)
    department = models.TextField(max_length=200,blank=True)
    work_discription  = models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.first_name

class Fish(models.Model):
    image = models.ImageField(upload_to="Image" ,blank=True)
    name = models.TextField(max_length=200,blank=True)
    type = models.TextField(max_length=200,blank=True)
    #exp_harv_date = models.DateTimeField(auto_now_add=True,blank=True)
    total = models.IntegerField(blank=True)

    def __str__(self):
        return self.name



