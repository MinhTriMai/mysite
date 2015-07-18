from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from form.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            senderName = form.cleaned_data['sender_name']
            senderEmail = form.cleaned_data['sender_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']            

            recipients = ['admin@ciscer.com']

            try:
                send_mail('[ciscer contact]' + ' From: ' + senderName + ' - ' + ' Subject: ' + subject, message, senderEmail, recipients, fail_silently=False) 
            except e:
                return HttpResponseRedirect('/thank-you/?m=fail')
            return HttpResponseRedirect('/thank-you/?m=success')
            
    else:
        form = ContactForm() # An unbound form
        
    return render(request, 'contact.html', {
        'form': form,
    })