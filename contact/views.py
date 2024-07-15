from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import MessageForm
from django.conf import settings


# To display and process the message form
def message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            # We send the email using the form information
            send_mail(
                subject=f"New message from {message.name}",
                message=message.content,
                from_email=message.email,
                recipient_list=[settings.EMAIL_HOST_USER],  # List of email recipients (your email)
                fail_silently=False,  # If sending the email fails, it will show an error
            )
            return redirect('success')
    else:
        # If the request is GET, we will display an empty form to the user
        form = MessageForm()
    return render(request, 'home.html', {'form': form})


# View to display the success page after submitting the form
def success_view(request):
    return render(request, 'home.html')
