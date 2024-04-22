from django import forms
from django.forms import ModelForm
from students.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'graduation_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['ssn'].widget.attrs['class'] = 'form-control'
        self.fields['ssn'].widget.attrs['placeholder'] = 'Enter SSN'
        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['graduation_date'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter Address'
        self.fields['address'].widget.attrs['rows'] = '5'
        self.fields['driver_license_number'].widget.attrs['class'] = 'form-control'
        self.fields['driver_license_number'].widget.attrs['placeholder'] = 'Enter Driver License Number'
        self.fields['driver_license_class'].widget.attrs['class'] = 'form-control'
        self.fields['state_issued'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        self.fields['transcript_file'].widget.attrs['class'] = 'files'
        self.fields['id_file'].widget.attrs['class'] = 'files'
        self.fields['application_file'].widget.attrs['class'] = 'files'
        self.fields['driver_license_file'].widget.attrs['class'] = 'files'
        self.fields['medical_card_file'].widget.attrs['class'] = 'files'
        self.fields['birth_certificate_file'].widget.attrs['class'] = 'files'
        self.fields['drug_screening_file'].widget.attrs['class'] = 'files'
        self.fields['miscellaneous_file'].widget.attrs['class'] = 'files'
