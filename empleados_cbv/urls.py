from django.urls import path
from . import views

urlpatterns = [
    # Position CRUD
    path('positions/', views.PositionListView.as_view(), name='position_list_cbv'),
    path('positions/create/', views.PositionCreateView.as_view(), name='position_create_cbv'),
    path('positions/<int:pk>/update/', views.PositionUpdateView.as_view(), name='position_update_cbv'),
    path('positions/<int:pk>/delete/', views.PositionDeleteView.as_view(), name='position_delete_cbv'),

    # Employee CRUD  ← COMPLETA TÚ ESTAS (5 rutas)
    path('employees/', views.EmployeeListView.as_view(), name='employee_list_cbv'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create_cbv'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail_cbv'),
    path('employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update_cbv'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete_cbv'),
]
