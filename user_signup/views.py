from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm



# Create your views here.
def login(request):
    return render(request, 'user_signup/index.html')

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, 'mkush.1112@gmail.com', [to_email])
            return render(request, 'user_signup/send_messages.html')
    else:
        form = EmailForm()
    
    return render(request, 'user_signup/index.html', {'form': form})