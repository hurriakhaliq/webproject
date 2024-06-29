from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    year_start = models.IntegerField()
    year_end = models.IntegerField()

    def __str__(self):
        return self.degree

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    responsibilities = models.TextField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_url = models.URLField()

    def __str__(self):
        return self.title

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class OwnerDetails(models.Model):
    name = models.CharField(max_length=100)
    intro = models.TextField()
    about = models.TextField()
    image_url = models.URLField()
    hero_image_url = models.URLField()

    def __str__(self):
        return self.name
