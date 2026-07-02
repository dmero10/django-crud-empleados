from django.urls import path
from . import views

urlpatterns = [
    # Position CRUD
    path('positions/', views.position_list, name='position_list'),
    path('positions/create/', views.position_create, name='position_create'),
    path('positions/<int:position_id>/update/', views.position_update, name='position_update'),
    path('positions/<int:position_id>/delete/', views.position_delete, name='position_delete'),

    # Employee CRUD
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:employee_id>/update/', views.employee_update, name='employee_update'),
    path('employees/<int:employee_id>/delete/', views.employee_delete, name='employee_delete'),
]
