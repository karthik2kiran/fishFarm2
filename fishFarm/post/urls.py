from django.urls import path

from .views import DamShow, home_view, DamEdit, DamDelete, DamView, DepartmentView, DepartmentShow, DepartmentEdit, \
    DepartmentDelete, StaffView, StaffShow, StaffEdit, StaffDelete, FishShow, FishView, FishDelete, FishEdit, \
    admin_dashboard_view, admin_click_view, afterlogin_view
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[

    path('', home_view, name=''),
    path('afterlogin', afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('adminclick', admin_click_view),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'), name='adminlogin'),
    path('admindashboard',admin_dashboard_view,name='admindashboard'),
    path('',home_view,name='home'),
    path('dview',DamView,name="d_view"),
    path('dshow',DamShow, name="d_show"),
    path('dedit/<int:id>', DamEdit, name="d_edit"),
    #path('dupdate/<int:id>', DamUpdate),
    path('ddelete/<int:id>', DamDelete),

    path('depview',DepartmentView,name="dep_view"),
    path('depshow',DepartmentShow, name="dep_show"),
    path('depedit/<int:id>', DepartmentEdit, name="dep_edit"),
    path('depdelete/<int:id>', DepartmentDelete),

    path('staffview',StaffView,name="staff_view"),
    path('staffshow',StaffShow, name="staff_show"),
    path('staffedit/<int:id>', StaffEdit, name="staff_edit"),
    path('staffdelete/<int:id>', StaffDelete),

    path('fishview',FishView,name="fish_view"),
    path('fishshow',FishShow, name="fish_show"),
    path('fishedit/<int:id>', FishEdit, name="fish_edit"),
    path('fishdelete/<int:id>', FishDelete),


    ]