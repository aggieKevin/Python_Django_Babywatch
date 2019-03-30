from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

#from polls.forms import RegistrationForm
#from .models import Question, Event



def home(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'main/home.html')

def register(request):
    
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/main')
    else:
        form=UserCreationForm()
        return render(request,'main/reg_form.html',{'form':form})
