from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Home, About, Profile, Category, Skills, Project

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Form submitted")
            print(form.cleaned_data)
            return redirect("index")
        else:
            messages.warning(request, "Invalid form submission")
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