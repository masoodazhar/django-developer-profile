from django.shortcuts import render
from .models import Home, WhatIDo, AboutMe, Testimonial, Client, FunFact, Education, Experience, Skill, Resume, Blog, Contact, socialLink
# Create your views here.
def index(request):
    home = Home.objects.last()
    aboutMe = AboutMe.objects.last()
    whatIDo = WhatIDo.objects.all()
    testimonial = Testimonial.objects.all()
    client = Client.objects.all()
    funFact = FunFact.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    resume = Resume.objects.last()
    blog = Blog.objects.all()
    contact = Contact.objects.last()
    sociallink = socialLink.objects.all()

    context = {
        'home': home,
        'aboutMe': aboutMe,
        'whatIDo': whatIDo,
        'testimonial': testimonial,
        'client': client,
        'funFact': funFact,
        'education': education,
        'experience': experience,
        'skill': skill,
        'resume': resume,
        'blog': blog,
        'contact': contact,
        'sociallink': sociallink
    }

    return render(request, 'index.html', context)