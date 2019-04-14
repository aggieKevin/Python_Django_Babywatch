from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreationForm
from .forms import HouseholdForm, GuardianForm, ChildForm,RatingForm
from .models import Household,Child,Guardian,Rating
#from polls.forms import RegistrationForm
#from .models import Question, Event

def home(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'main/home.html')

def about(request):
    return render (request,'main/About.html')

def register(request):

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Your account has been created')
            form.save()
            return redirect('/main/createprofile/')
    else:
        form=UserCreationForm()
        return render(request,'main/register.html',{'form':form})

def createprofile(request):
    if request.method=='POST':
        form=HouseholdForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/main')
    else:
        form=HouseholdForm()
        return render(request,'main/createprofile.html',{'form':form})

def createguardian(request):
    if request.method=='POST':
        form=GuardianForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/main')
    else:
        form=GuardianForm()
        return render(request,'main/createguardian.html',{'form':form})

def createchild(request):
    if request.method=='POST':
        form=ChildForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/main')
    else:
        form=ChildForm()
        return render(request,'main/createprofile.html',{'form':form})
''' another way
def my_view(request, id):
    instance = get_object_or_404(MyModel, id=id)
    form = MyForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('next_view')
    return render(request, 'my_template.html', {'form': form})
'''
def updateprofile(request):
    instance=Household.objects.filter(user=request.user).first()
    if request.method=='POST':
        form=HouseholdForm(request.POST,instance=instance)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/main')
    else:
        if instance:
            form=HouseholdForm(instance=instance)
        else:
            form=HouseholdForm()
        return render(request,'main/updateprofile.html',{'form':form})
'''
def updateguardian(request):
    instance=Household.objects.filter(user=request.user).first()
    if request.method=='POST':
        if instance:
            form=HouseholdForm(request.POST,instance=instance)
        else:
            form=HouseholdForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/main')
    else:
        if instance:
            form=HouseholdForm(instance=instance)
        else:
            form=HouseholdForm()
        return render(request,'main/updateprofile.html',{'form':form})
'''

def updateguardian(request):
	forms=[]
	#lst=[]
	instances=Guardian.objects.filter(household=request.user)
	if request.method=='POST':
		for i in range(len(instances)):
			if (i in request.POST) or (str(i) in request.POST):
				instance=instances[i]
				form=GuardianForm(request.POST,instance=instance)
				if form.is_valid():
					form.save()
					return redirect('/main')

	else:
		i=0
		for instance in instances:
			form=GuardianForm(instance=instance)
			forms.append([form,str(i)])
			i+=1
		return render(request,'main/updateguardian.html',{'forms':forms})

def updatechild(request):
	forms=[]
	#lst=[]
	instances=Child.objects.filter(household=request.user)
	if request.method=='POST':
		for i in range(len(instances)):
			if (i in request.POST) or (str(i) in request.POST):
				instance=instances[i]
				form=ChildForm(request.POST,instance=instance)
				if form.is_valid():
					form.save()
					return redirect('/main')

	else:
		i=0
		for instance in instances:
			form=ChildForm(instance=instance)
			forms.append([form,str(i)])
			i+=1
		return render(request,'main/updatechild.html',{'forms':forms})

def search(request):
    city_get=request.GET.get("city")
    house_list=Household.objects.filter(city=city_get)
    family_list=[]
    for house in house_list:
        user=house.user
        guard=Guardian.objects.filter(household=user).first()
        child=Child.objects.filter(household=user).first()
        ratings=Rating.objects.filter(receiver=house)
        if ratings:
            score=0
            for r in ratings:
                score+=r.rate
            av_rating=int(score/len(ratings))
        else:
            av_rating=5
        family_list.append((house,guard,child,av_rating))
    content={'family_list':family_list}
    return render(request,'main/search.html',content)




def detail(request,household_id):

    house=get_object_or_404(Household, pk=household_id)
    if request.method=='POST':
        form=RatingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.receiver=get_object_or_404(Household, pk=1)
            try:
                post.giver=(Household.objects.get(user=request.user)).household_name
            except:
                post.giver=' '
            post.save()
            return redirect('/main/search')
    else:
        user=house.user
        guard=Guardian.objects.filter(household=user).first()
        child=Child.objects.filter(household=user).first()
        template='main/detail.html'
        form=RatingForm()
        content={'house':house,'child':child,'guard':guard, 'form':form}
        return render(request,template,content)
