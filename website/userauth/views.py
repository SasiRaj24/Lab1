from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = forms.Register(request.POST)
		if form.is_valid():
			form.save()
			models.Otherdetail(
				user=User.objects.get(username=form.cleaned_data.get('username')),
				bio=form.cleaned_data.get('bio'),
				dob=form.cleaned_data.get('date_of_birth')
				).save()
			return HttpResponse("user saved")
		else:
			return render(request,'userauth/signup.html',{'form' : form})
	else:
		form = forms.Register()
	return render(request,'userauth/signup.html',{'form' : form})