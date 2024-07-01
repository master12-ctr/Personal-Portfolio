from django.shortcuts import render, redirect

# Create your views here.
from .forms import ContactForm
from .models import Contact
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from Home.models import CustomUser
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'message', 'phone_number', 'attachment' ]
    first_user=CustomUser.objects.first()
    template_name = 'Contact/contact_form.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Message send successfully!")
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['user'] = CustomUser.objects.first()
     return context

class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'message', 'phone_number', 'attachment']


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contact_form")


def create_Message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           # Send email with the response
           # email_subject = 'Thank you for your message'
           #email_message = 'Thank you for your message. We appreciate your feedback.'
           # send_mail(email_subject, email_message, settings.DEFAULT_FROM_EMAIL, [form.cleaned_data['email']])
           # messages.success(request, "Message send successfully!")
            return redirect("home")
    else:
        form = ContactForm()
    
    User = CustomUser.objects.first()
    
    context = {
        'form': form,
        'user': User
    }
    
    return render(request, 'Contact/contact_form.html', context)