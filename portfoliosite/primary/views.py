from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import ContactForm
from .models import Contact

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from portfoliosite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, BadHeaderError
from . import forms
from portfoliosite import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from decouple import config

# Create your views here.
class IndexView(TemplateView):
    template_name = 'contact.html'

class ContactFormView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    model = Contact
    redirect_field_name = 'index.html'
    def form_valid( self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('Name'),
            email=form.cleaned_data.get('Email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))

        send_mail(
            subject='A Message from Oshiro-Codes',
            message=message,
            from_email='email',
            recipient_list=[config('EMAIL_HOST_USER')],
            fail_silently = False
            )
        def mailsent(request):
            return render(request, 'index.html')
        return super(ContactFormView, self).form_valid(form)
