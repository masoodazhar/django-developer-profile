from django.contrib import admin
from .models import Home, WhatIDo, AboutMe, Testimonial, Client, FunFact, Education, Experience, Skill, SkillCategory, Resume, PortFolioTab, PortFolio, Blog, Contact, socialLink

admin.site.site_header = "Full Stack Python Developer"
admin.site.site_title = "Full Stack"
admin.site.index_title = "Masood Azhar Profile"

admin.site.register([Home, WhatIDo, AboutMe, Testimonial, Client, FunFact, Education, Experience, Skill, SkillCategory, Resume, PortFolioTab, PortFolio, Blog, Contact, socialLink])