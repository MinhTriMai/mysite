from django import forms

class ContactForm(forms.Form):
    sender_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'required': "", 'pattern': "^.{1,100}$", 'class': "radius"}), max_length=100, error_messages = {'required': 'Please enter your name.'})
    sender_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email', 'type': "email", 'required': "", 'class': "radius"}), error_messages = {
        'required': 'Your email is required.',
        'invalid': 'Please enter a valid email.'
    })
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject', 'required': "", 'class': "radius"}), max_length=100, error_messages = {'required': 'Please enter the email subject.'})
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'required': "", 'class': "radius"}), max_length=5000, error_messages = {'required': 'Please enter your message.'})
    