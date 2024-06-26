from django import forms
from django.forms import ModelForm
from .models import Student

class AddStudentForm(ModelForm):
    YEAR_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]

    COURSE_CHOICES = [
        ('BSIT', 'Bachelor of Science in Information Technology'),
        ('BSCE', 'Bachelor of Science in Computer Engineering'),
    ]

    year = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    course = forms.ChoiceField(choices=COURSE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birth_date', 'mobile_num', 'email', 'address', 'year', 'course']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Juan'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Dela Cruz'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'max': '9999-12-31', 'value':'2024-01-01'}),
            'mobile_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 09123456789', 'pattern': '[0-9]{11}', 'title': 'Mobile number must be 11 digits.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g. juan@gmail.com'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Quezon City'}),
        }