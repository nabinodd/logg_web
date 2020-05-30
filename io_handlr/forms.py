from django import forms
from django.forms import ModelForm
from .models import Visitor

# class DataEntryForm(forms.Form):
#     name=forms.CharField(label='Name',max_length=100)

class VisitorModelForm(ModelForm):
    class Meta:
        model=Visitor
        fields='__all__'
        # fields=['name','addr','instu','phone','remarks','date','chk_in_time','chk_out_time','img_name']

