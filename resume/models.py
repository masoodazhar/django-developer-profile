from django.db import models

# Create your models here.



class Home(models.Model):
    background_image = models.ImageField(upload_to='images')
    heading = models.CharField(max_length=200)
    skills = models.TextField()

    def __str__(self) -> str:
        return self.heading
    
    def get_skills(self):
        return str(self.skills).split('>')

class WhatIDo(models.Model):
    icon = models.CharField(max_length=50 ,default='lnr lnr-store')
    heading = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.heading
    
class AboutMe(models.Model):
    profile_image = models.ImageField(upload_to='images')
    heading = models.CharField(max_length=200)
    description = models.TextField()
    age = models.IntegerField()
    residence = models.CharField(max_length=255)
    Address = models.TextField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.heading
    

class Testimonial(models.Model):
    image = models.ImageField(upload_to='images')
    heading = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.heading

class Client(models.Model):
    logo = models.ImageField(upload_to='images')
    link = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.link
    
class FunFact(models.Model):
    icon = models.CharField(max_length=50 ,default='lnr lnr-smile')
    heading = models.CharField(max_length=29)
    numbers = models.IntegerField()

    def __str__(self) -> str:
        return self.icon
    
class Education(models.Model):
    uni_name = models.CharField(max_length=100)
    year = models.IntegerField()
    field = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.uni_name

class Experience(models.Model):
    from_year = models.CharField(max_length=50)
    to_year = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    heading = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.heading

class SkillCategory(models.Model):
    heading = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.heading

   
class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, verbose_name='category', related_name='category')
    heading = models.CharField(max_length=50)
    skill_time = models.IntegerField()

    def __str__(self) -> str:
        return self.heading
    

class Resume(models.Model):
    resume = models.FileField(upload_to='files')

class PortFolio(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50 ,default='lnr lnr-smile')
    image = models.ImageField(upload_to='images')
    link = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
class Blog(models.Model):
    heading = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    date = models.DateField()
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.heading

class Contact(models.Model):
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    freelance_avalaible = models.BooleanField()

    def __str__(self) -> str:
        return self.phone

class socialLink(models.Model):
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.linkedin