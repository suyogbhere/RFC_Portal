from myapp.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


class Signupform(UserCreationForm):
    password1= forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model : User
        fields=['username','first_name','last_name','email']
        labels={"first_name":"First Name","last_name":"Last Name","email":"Email"}
        widgets={"username":forms.TextInput(attrs={"class":"form-control"}),
                 "first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "last_name":forms.TextInput(attrs={"class":"form-control"}),
                 "email":forms.EmailInput(attrs={"class":"form-control"}),
                 }
        
#Password Changeform
class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label='Old_Password',strip=False,widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))
    new_password1=forms.CharField(label='New_Password',strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label='Confirm_Password',strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))


environment=[
    ('PROD','PROD'),
    ('DR','DR'),
    ('UAT','UAT'),
    ('PREPROD','PREPROD')
]

Change_level=[
    ('Major','Major'),
    ('Minor','Minor'),
    ('Normal','Normal')
]

Risk_Rating=[
    ('medium','medium'),
    ('very high','very high'),
    ('low','low'),
    ('High','High')
]

status=[
    ('APPROVED','APPROVED'),
    ('REJECTED','REJECTED'),
    ('HOLD','HOLD'),
    ('CANCELLED','CANCELLED'),
    ('ROLLBACK','ROLLBACK'),
    ('CLOSED','CLOSED')
]

class RFC_Raised_Form(forms.ModelForm):
    Environment = forms.MultipleChoiceField(choices=environment, widget=forms.CheckboxSelectMultiple)
    Change_level = forms.ChoiceField(choices=Change_level, widget=forms.RadioSelect)
    Risk_Rating = forms.ChoiceField(choices=Risk_Rating,widget=forms.RadioSelect)
    
    class Meta:
        model = RFC_Register
        fields = "__all__"
        widgets={
            'Reference_RFC_No':forms.TextInput(attrs={'class':'form-control'}),
            'Department': forms.Select(attrs={'class':'form-select'}),
            'Request_Type': forms.Select(attrs={'class':'form-select'}),
            'Planned_Date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'Category': forms.Select(attrs={'class':'form-select'}),
            'Reason_for_change': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'Description_of_change': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'System_Details': forms.Select(attrs={'class':'form-select'}),
            'To_be_executed_by': forms.Select(attrs={'class':'form-select'}),
            'Change_Requested_by': forms.TextInput(attrs={'class':'form-control'}),
            'Change_authorizer': forms.Select(attrs={'class':'form-select'}),
            'Change_impact_assessment': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'Attachments': forms.FileInput(attrs={'class':'form-control'}),
            'Change_rollback_procedures': forms.Textarea(attrs={'class':'form-control','rows':3}),
        }


