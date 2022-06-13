from django import forms
from django.contrib.auth.models import User
from . import models



class DamForm(forms.ModelForm):
    class Meta :
        model = models.Dam
        fields = ['name','image','no_fishes','category','location','about']


class New_departmentForm(forms.ModelForm):
    class Meta:
        model = models.New_department
        fields = ['dep_name','dep_discription']


class StaffForm(forms.ModelForm):
    class Meta :
        model = models.Staff
        fields = ['first_name','last_name','salary','mobile','state','country','department','work_discription']



class FishForm(forms.ModelForm):
    class Meta:
        model = models.Fish
        fields = ['image','name','type','total']


