from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .views import *
from .models import Contact
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def hi(request):

    
    return render(request,'index.html')


def contact(request):
     
    if  request.method == "POST": 
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        desc=request.POST.get('desc')
        
        from_email=settings.EMAIL_HOST_USER

        if len(name)<4 or len(subject)<4 or len(desc)<4 :
            messages.error(request," Username & subject & desc, must contain atleast 4 Characters..")
            return redirect('/')
        

     

        

        else:
            connection=mail.get_connection()
            connection.open()
            emaill=mail.EmailMessage(name  , "\n email adress of user : "+ email + "\n Description : " + desc   + "\n Subject : " + subject + "\n ThankYou For Sending Message...." ,from_email,['manjunathgowda7826@gmail.com'],connection=connection)
            
            connection.send_messages([emaill])
            connection.close()
            connection=mail.get_connection()
            connection.open()
            emailll=mail.EmailMessage( "Hi " + name  ,  " ThankYou For Sending Message...." + "\n Your Feedback is added value for us Thank you once Again,Good Luck" + "\n ...by MANJUNATH" ,from_email,[email],connection=connection)
            connection.send_messages([emailll])
            connection.close()
            contact=Contact(name=name,email=email,subject=subject,desc=desc)
            contact.save()
            messages.success(request," Your Message had been sent Successfully...")
                 


    return redirect('/') 