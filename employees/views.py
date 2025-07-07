from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def staff_required(user):
    return user.is_staff

@login_required
@user_passes_test(staff_required)
def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees':employee})


@login_required
@user_passes_test(staff_required)
def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employees/employee_form.html', {'form': form})


@login_required
@user_passes_test(staff_required)
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})


@login_required
@user_passes_test(staff_required)
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employees/employee_form.html',{'form': form})

@login_required
@user_passes_test(staff_required)
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/confirm_delete.html', {'employee': employee})

