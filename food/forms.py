from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm



# class ResetPasswordForms(PasswordResetForm):
#     def __init__(self,*args,**kwargs):
#         super(ResetPasswordForms,self).__init__(*args,**kwargs)

#     email = forms.CharField(widget=forms.TextInput(attrs=
#     {
#         "class":"form-control form-control-lg",
#         "type":"email",
#         "placeholder":"Enter Email",
        
#     }))

# class NewPasswordForms(SetPasswordForm):
#     def __init__(self,*args,**kwargs):
#         super(NewPasswordForms,self).__init__(*args,**kwargs)

#     new_password1 = forms.CharField(widget=forms.PasswordInput(attrs=
#     {
#         "class":"form-control form-control-lg",
#         "type":"password",
#         "placeholder":"New Password ",
#         "autocomplete":"new-password",
#     }))

#     new_password2 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs=
#     {
#         "class":"form-control form-control-lg",
#         "type":"password",
#         "placeholder":"Confirm Password",
#         "autocomplete":"new-password",
        
#     }))