from django.shortcuts import render, redirect
from .models import Education, Experience, Skill, Project, OwnerDetails
from .forms import ContactForm

def home(request):
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    owner_details = OwnerDetails.objects.first()  # Assuming there's only one owner

    context = {
        'education': educations,
        'experience': experiences,
        'skills': skills,
        'projects': projects,
        'owner_details': owner_details,
    }

    return render(request, 'main/home.html', context)

def contact_form_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'main/home.html', {'form': form})
