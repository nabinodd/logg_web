from django.http import HttpResponse
from django.shortcuts import render

from .forms import VisitorModelForm
from .models import Visitor

from django.contrib import messages

def data_entry(request):

    if request.method == 'POST':
        form = VisitorModelForm(request.POST)
        if form.is_valid():
            form.save()
            print('Saved')
    form=VisitorModelForm
    all_data=Visitor.objects.all()
    return render(request,'tst.html',{'form':form,'data':all_data})
    