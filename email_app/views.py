import os
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import UserSignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from email.mime.image import MIMEImage
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError




class MyTemplateView(TemplateView):
    template_name = 'hello_email.html'

    # https://stackoverflow.com/questions/1633109/creating-a-mime-email-template-with-images-to-send-with-python-django
    def logo_data(self, image_name):
        print(f"{image_name} was added to the mail attachment")
        with open(os.path.join(settings.MEDIA_ROOT, image_name), 'rb') as f:
            logo_data = f.read()
        logo = MIMEImage(logo_data)
        logo.add_header('Content-ID', f'<{image_name}>')
        logo.add_header('Content-Disposition', 'inline', filename=image_name)

        return logo

    def get(self, request, *args, **kwargs):
        html_message = render_to_string(self.template_name, context={'email': True})

        email_message = EmailMultiAlternatives(subject='Subject',
                                               body='text_content',
                                               from_email='from@gmail.com',
                                               to=['nyckolas.python@gmail.com'])
        email_message.attach_alternative(html_message, 'text/html')
        email_message.mixed_subtype = 'related'
        for image in os.listdir(settings.MEDIA_ROOT):
            email_message.attach(self.logo_data(image))
        email_message.send(fail_silently=False)
        # function to send email
        # send_mail('Subject', 'Hello', 'from@nyckolas.com', ['nyckolas.python@gmail.com'],
        #           fail_silently=True,
        #           html_message=html_message)
        return render(request, self.template_name)

def usersignup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse(
                'We have sent you an email, please confirm your email address to complete registration')
    else:
        form = UserSignUpForm()
    return render(request, 'signup.html', {'form': form})


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')


api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID


# Subscription Logic
def subscribe(email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))


def subscription(request):
    if request.method == "POST":
        email = request.POST['email']
        print(email)
        subscribe(email)
        messages.success(request, "Email received. thank You! ")

    return render(request, "subscription.html")
