from django.shortcuts import render
from .models import Home, WhatIDo, AboutMe, Testimonial, Client, FunFact, Education, Experience, Skill, SkillCategory, Resume, PortFolioTab, PortFolio, Blog, Contact, socialLink
from django.http import JsonResponse
from django.core.mail import send_mail
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
    skillCategory = SkillCategory.objects.all()
    skill = Skill.objects.all()
    resume = Resume.objects.last()
    portFolioTab = PortFolioTab.objects.all()
    portFolio = PortFolio.objects.all()
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
        'skillCategory': skillCategory,
        'skill': skill,
        'resume': resume,
        'portFolio': portFolio,
        'portFolioTab': portFolioTab,
        'blog': blog,
        'contact': contact,
        'sociallink': sociallink
    }

    return render(request, 'index.html', context)


def sendMail(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'masoodazhar60@gmail.com',
        ['intel3xcel@gmail.com'],
        fail_silently=False,
    )
    return JsonResponse({'type': 'success', 'message': 'Mail has been send!'})