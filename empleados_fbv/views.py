from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Position, Employee
from .forms import PositionForm, EmployeeForm


#POSITION CRUD (Function-Based Views)

#read
@login_required
def position_list(request):
    positions = Position.objects.all()
    return render(request, 'empleados_fbv/position_list.html', {'positions':positions})


#create
@login_required
def position_create(request):
    if request.method == 'GET':
        return render(request, 'empleados_fbv/position_form.html', {'form': PositionForm()})
    else:
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('position_list')
        return render(request, 'empleados_fbv/position_form.html', {'form': form})

    
        
#Update
@login_required
def position_update(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    if request.method == 'GET':
        form = PositionForm(instance=position)
        return render(request, 'empleados_fbv/position_form.html', {'form': form})
    else:
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('position_list')
        return render(request, 'empleados_fbv/position_form.html', {'form': form})
    
    
    
#Delete
@login_required
def position_delete(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    if request.method == 'POST':
        position.delete()
        return redirect('position_list')
    return render(request, 'empleados_fbv/position_confirm_delete.html', {'position': position})





# EMPLOYEE CRUD (Function-Based Views)

# READ
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'empleados_fbv/employee_list.html', {'employees': employees})


# READ
@login_required
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'empleados_fbv/employee_detail.html', {'employee': employee})


# CREATE
@login_required
def employee_create(request):
    if request.method == 'GET':
        return render(request, 'empleados_fbv/employee_form.html', {'form': EmployeeForm()})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        return render(request, 'empleados_fbv/employee_form.html', {'form': form})


# UPDATE
@login_required
def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'GET':
        form = EmployeeForm(instance=employee)
        return render(request, 'empleados_fbv/employee_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        return render(request, 'empleados_fbv/employee_form.html', {'form': form})


# DELETE
@login_required
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'empleados_fbv/employee_confirm_delete.html', {'employee': employee})
