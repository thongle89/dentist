from django.shortcuts import render
from django.core.mail import send_mail

from django.utils.translation import gettext_lazy as _

def home(request):
	return render(request,'home.html',{})

def about(request):
	return render(request,'about.html',{})

def service(request):
	return render(request,'service.html',{})

def pricing(request):
	return render(request,'pricing.html',{})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email =request.POST['message-email']
		message = request.POST['message']

		#send an email
		send_mail(
			message_name, #subject
			message, #message
			message_email, # from email
			['quangthong2366@gmail.com'], #to email

			)

		return render(request,'contact.html',{'message_name':message_name})
	else:
		return render(request,'contact.html',{})
