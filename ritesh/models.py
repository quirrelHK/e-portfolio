from django.db import models
from PIL import Image

# Home Section
class Home(models.Model):
    name = models.CharField(max_length=30)
    greetings_1 = models.CharField(max_length=10)
    greetings_2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to="picture/")
    resume = models.FileField(upload_to='resume/', null=True, default=None)
    # Save time when modified
    updated = models.DateTimeField(auto_now=True)
    
    # Overriding the save method to resize the images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.picture.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    def __str__(self) -> str:
        return self.name
    
    
# About Section
class About(models.Model):
    heading = models.CharField(max_length=100)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.career

class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_media = models.CharField(max_length=20)
    link = models.URLField(max_length=200)
    
# Skills Section
class Category(models.Model):
    name = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        
    def __str__(self) -> str:
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=30)
    

# Portfolio Section

class Project(models.Model):
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='project/')
    name = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return f"Project {self.id}"