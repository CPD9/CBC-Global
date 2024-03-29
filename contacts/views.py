from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    project_id = request.POST['project_id']
    project = request.POST['project']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']

    # Accessing superuser
    superuser = User.objects.filter(is_superuser=True)
    superuser_email = User.objects.filter(is_superuser=True).values_list('email')

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(project_id=project_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this project.')
        return redirect('/projects/'+project_id)

    contact = Contact(project=project, project_id=project_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email
    send_mail(
      'Project Inquiry',
      'There has been an inquiry for ' + project + '. Sign into the admin panel for more info',
      'dikepeter9@gmail.com',
      ['dikepeter9@yahoo.com'],
      fail_silently=False
    )

    messages.success(request, 'Your request has been submitted, we will get back to you soon.')
    return redirect('/projects/'+project_id)