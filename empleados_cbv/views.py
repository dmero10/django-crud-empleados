from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from empleados_fbv.models import Position, Employee   # importamos los modelos de la otra app
from empleados_fbv.forms import PositionForm, EmployeeForm


class PositionListView(ListView):
    model = Position                             # ¿qué modelo?
    template_name = 'empleados_cbv/position_list.html'                    # ¿qué plantilla? (ruta 'empleados_cbv/...')
    context_object_name = 'positions'                # ¿cómo se llamará la lista en la plantilla?



class PositionCreateView(CreateView):
    model = Position
    form_class =  PositionForm
    template_name = 'empleados_cbv/position_form.html'
    success_url = reverse_lazy('position_list_cbv')


class PositionUpdateView(UpdateView):
    model = Position
    form_class = PositionForm
    template_name = 'empleados_cbv/position_form.html'        # ¡la misma del form! (crear y editar comparten plantilla)
    success_url = reverse_lazy('position_list_cbv')
    
    
class PositionDeleteView(DeleteView):
    model = Position
    template_name = 'empleados_cbv/position_confirm_delete.html'         # la de confirmar: 'empleados_cbv/position_confirm_delete.html'
    success_url = reverse_lazy('position_list_cbv')


# ---------- EMPLOYEE CRUD (Class-Based Views) ----------
# LoginRequiredMixin = el equivalente en clases del @login_required de las funciones.
# Se pone ANTES de la vista genérica para exigir estar logueado.

# READ: list all employees
class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'empleados_cbv/employee_list.html'
    context_object_name = 'employees'


# READ: detail of one employee
class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'empleados_cbv/employee_detail.html'
    context_object_name = 'employee'


# CREATE: new employee
class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'empleados_cbv/employee_form.html'
    success_url = reverse_lazy('employee_list_cbv')


# UPDATE: edit an existing employee
class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'empleados_cbv/employee_form.html'
    success_url = reverse_lazy('employee_list_cbv')


# DELETE: remove an employee
class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'empleados_cbv/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list_cbv')
