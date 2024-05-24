import os
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Home, About, Profile, Category, Skills, Project

def index(request):
    # storage = messages.get_messages(request)
    # for message in storage:
    #     print(message)
    # storage.used = True
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Thanks for reaching out, will get back to you shortly.")
            send_mail(
                f"Reaching Out | {form.cleaned_data.get('name')}",
                f"{form.cleaned_data.get('message')} \n\n{form.cleaned_data.get('email')}",
                os.environ.get("EMAIL_HOST_USER"),
                ["riteshsingh9827@gmail.com"],
                fail_silently=False,
            )

            # print(form.cleaned_data)
        else:
            # print("Not valid")
            messages.warning(request, "It seems your details for not valid.")

        return redirect("http://localhost:8000/#home")
    else:
        form = ContactForm()
    # Home
    home = Home.objects.latest('updated')
    
    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    
    # Skills
    categories = Category.objects.all()
    
    # Projects
    projects = Project.objects.all()
    
    context = {
        "home":home,
        "about":about,
        "profiles":profiles,
        "categories":categories,
        "projects":projects,
        "form":form
        
    }
    
    
    return render(request, "index.html", context)