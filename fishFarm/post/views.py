import os

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.

from .forms import DamForm
from .models import Dam, New_department, Staff, Fish

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'admin_base.html')


# for showing login button for admin(by sumit)
def admin_click_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


def admin_dashboard_view(request):
    products = Dam.objects.all()
    context = {'products': products}
    return render(request, 'admin_dashboard.html', context)


# -----------for checking user isuser
def is_user(user):
    return user.groups.filter(name='USER').exists()


# ---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,CUSTOMER

def afterlogin_view(request):
    if is_user(request.user):
        return redirect('navbar')

    else:
        return redirect('admindashboard')

#Dam
'''
def DamView(request):
    if request.method == 'POST':
        form = DamForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            dam=form.instance
            return redirect('/dshow')
    else:
        form = DamForm()
    return render(request, 'dam/add.html', {'form': form})
'''

def DamView(request):
    if request.method == "POST":
        dam = Dam()
        dam.name = request.POST.get('name')
        dam.category = request.POST.get('category')
        dam.no_fishes = request.POST.get('no_fishes')
        dam.location = request.POST.get('location')
        dam.about = request.POST.get('about')

        if len(request.FILES) != 0:
            dam.image = request.FILES['image']

        dam.save()
        messages.success(request, "Product Added Successfully")
        return redirect('/dshow')
    return render(request, 'dam/add.html')
'''
def DamEdit(request, id):
    dam = Dam.objects.get(id=id)
    return render(request, 'dam/edit.html', {'dam': dam})
'''
def DamShow(request):
    dams = Dam.objects.all()
    return render(request, 'dam/show.html', {'dams': dams})

def DamEdit(request, id):
    dam = Dam.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(dam.image) > 0:
                os.remove(dam.image.path)
            dam.image = request.FILES['image']
        dam.name = request.POST.get('name')
        dam.no_fishes = request.POST.get('no_fishes')
        dam.category = request.POST.get('category')
        dam.location = request.POST.get('location')
        dam.about = request.POST.get('about')
        dam.save()
        messages.success(request, "details Updated Successfully")
        return redirect('/dshow')

    context = {'dam':dam}
    return render(request, 'dam/edit.html', context)



def DamDelete(request, id):
    dam =Dam.objects.get(id=id)
    if len(dam.image) > 0:
        os.remove(dam.image.path)
    dam.delete()
    return redirect('/dshow')

# DEPARTMENT

def DepartmentView(request):
    if request.method == "POST":
        department = New_department()
        department.dep_name = request.POST.get('dep_name')
        department.dep_discription = request.POST.get('dep_discription')

        department.save()
        messages.success(request, "Department Added Successfully")
        return redirect('/depshow')
    return render(request, 'department/add.html')

def DepartmentShow(request):
    departments = New_department.objects.all()
    return render(request, 'department/show.html', {'departments': departments})

def DepartmentEdit(request, id):
    department = New_department.objects.get(id=id)

    if request.method == "POST":
        department.dep_name = request.POST.get('dep_name')
        department.dep_discription = request.POST.get('dep_discription')

        department.save()
        messages.success(request, "details Updated Successfully")
        return redirect('/depshow')

    context = {'department':department}
    return render(request, 'department/edit.html', context)

def DepartmentDelete(request, id):
    department =New_department.objects.get(id=id)
    department.delete()
    return redirect('/depshow')

# Staff

def StaffView(request):
    if request.method == "POST":
        staf = Staff()
        staf.first_name = request.POST.get('first_name')
        staf.last_name = request.POST.get('last_name')
        staf.salary = request.POST.get('salary')
        staf.mobile = request.POST.get('mobile')
        staf.state = request.POST.get('state')
        staf.country = request.POST.get('country')
        staf.department = request.POST.get('department')
        staf.work_discription = request.POST.get('work_discription')

        staf.save()
        messages.success(request, "Staff Added Successfully")
        return redirect('/staffshow')
    return render(request, 'staff/add.html')

def StaffShow(request):
    staffs = Staff.objects.all()
    return render(request, 'staff/show.html', {'staffs': staffs})


def StaffEdit(request, id):
    staf = Staff.objects.get(id=id)

    if request.method == "POST":
        staf.first_name = request.POST.get('first_name')
        staf.last_name = request.POST.get('last_name')
        staf.salary = request.POST.get('salary')
        staf.mobile = request.POST.get('mobile')
        staf.state = request.POST.get('state')
        staf.country = request.POST.get('country')
        staf.department = request.POST.get('department')
        staf.work_discription = request.POST.get('work_discription')

        staf.save()
        messages.success(request, "details Updated Successfully")
        return redirect('/staffshow')

    context = {'staf':staf}
    return render(request, 'staff/edit.html', context)

def StaffDelete(request, id):
    staf =Staff.objects.get(id=id)
    staf.delete()
    return redirect('/staffshow')


# FISH

def FishView(request):
    if request.method == "POST":
        fish = Fish()
        fish.image = request.POST.get('image')
        fish.name = request.POST.get('name')
        fish.type = request.POST.get('type')
        fish.total = request.POST.get('total')

        if len(request.FILES) != 0:
            fish.image = request.FILES['image']

        fish.save()
        messages.success(request, "Fish Added Successfully")
        return redirect('/fishshow')
    return render(request, 'fish/add.html')


def FishShow(request):
    fishes = Fish.objects.all()
    return render(request, 'fish/show.html', {'fishes': fishes})

def FishEdit(request, id):
    fish = Fish.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(fish.image) > 0:
                os.remove(fish.image.path)
            fish.image = request.FILES['image']
        fish.name = request.POST.get('name')
        fish.type = request.POST.get('type')
        fish.total = request.POST.get('total')

        fish.save()
        messages.success(request, "fish Updated Successfully")
        return redirect('/fishshow')

    context = {'fish':fish}
    return render(request, 'fish/edit.html', context)

def FishDelete(request, id):
    fish =Fish.objects.get(id=id)
    if len(fish.image) > 0:
        os.remove(fish.image.path)
    fish.delete()
    return redirect('/fishshow')

