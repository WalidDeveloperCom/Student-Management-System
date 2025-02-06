from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
#    def clean_phone_number(self):
#       phone_number = self.cleaned_data.get('phone_number')
#        if not phone_number.isdigit():
#            raise forms.ValidationError("Phone number should contain only digits.")
#        if len(phone_number) > 15:
#            raise forms.ValidationError("Phone number should have at most 15 digits.")
#        return phone_number

    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_number', 'course']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
        }

