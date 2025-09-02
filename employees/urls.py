from django.urls import path
from . import views

urlpatterns = [
    path('api/employees/', views.employee_api, name='employee_api'),
    path('apply-bonus/', views.apply_bonus_view, name='apply_bonus'),
    path('report/', views.report_view, name='report'),
    path('', views.employee_list, name='employee_list'), 
]