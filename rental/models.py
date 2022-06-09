from django.db import models
import datetime as dt

class Properties(models.Model):
    title = models.CharField(max_length=60)
    location = models.CharField(max_length=30)
    propertyphotos = models.ImageField(upload_to = 'property/')
    description = models.TextField()
    price = models.FloatField()
    status = models.CharField(max_length=30)
    rooms = models.FloatField()
    period = models.CharField(max_length=15)
    
    @classmethod
    def property_details(cls):
        property = cls.objects.all()
        return property

    @classmethod
    def property_details(cls):
        property = cls.objects.filter()
        return property

class Blog(models.Model):
    title = models.CharField(max_length = 60)
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    blogimage = models.ImageField(upload_to = 'blog/')
    category = models.CharField(max_length=30)

    @classmethod
    def blog_details(cls):
        blog = cls.objects.all()
        return blog

class About(models.Model):
    title = models.CharField(max_length = 60)
    subtitle = models.TextField()
    headimage = models.ImageField(upload_to = 'about/')
    footimage = models.ImageField(upload_to = 'about/')
    heading = models.CharField(max_length = 60)
    description = models.TextField()

    @classmethod
    def about_details(cls):
        about = cls.objects.all()
        return about