from django.shortcuts import render, redirect, get_object_or_404
from .models import Students


def home(request):
    return render(request, 'index.html')


def student_list(request):
    students = Students.objects.all()
    ctx = {'students': students}
    return render(request, 'school/students-list.html', ctx)


def student_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        if (first_name and last_name and age
                and email):
            Students.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                email=email,
            )
            return redirect('students:list')
    return render(request, 'school/students-form.html')


def student_detail(request, pk):
    student = get_object_or_404(Students, pk=pk)
    ctx = {'student': student}
    return render(request, 'school/students-detail.html', ctx)


def student_delete(request, pk):
    student = get_object_or_404(Students, pk=pk)
    student.delete()
    return redirect('students:list')

