from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from .forms import AddStudentForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    query = request.GET.get('q')

    if query:
        query = query.strip()
        student_list = Student.objects.filter(
            Q(id__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(birth_date__icontains=query) |
            Q(mobile_num__icontains=query) |
            Q(email__icontains=query) |
            Q(address__icontains=query)
        )
    else:
        student_list = Student.objects.all()
    return render(request, 'main/index.html', {'student_list':student_list})

def add(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name'].upper()
            last_name = form.cleaned_data['last_name'].upper()
            email = form.cleaned_data['email']
            mobile_num = form.cleaned_data['mobile_num']

            if Student.objects.filter(
                Q(first_name=first_name, last_name=last_name) |
                Q(email=email) |
                Q(mobile_num=mobile_num)
            ).exists():
                messages.error(request, 'This student already exists.')
            else:
                student = form.save(commit=False)
                student.first_name = first_name
                student.last_name = last_name
                student.save()
                messages.success(request, f'"{student.first_name} {student.last_name}" has been added successfully.')
    
                # return redirect('index')
    elif request.method == 'GET':
        form = AddStudentForm()

    return render(request, 'main/add.html', {'form':form})