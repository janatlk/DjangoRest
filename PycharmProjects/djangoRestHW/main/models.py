from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500,blank=True,null=True)
    duration = models.TimeField()
    director = models.ForeignKey(to=Director,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(max_length=300)
    movie = models.ForeignKey(to=Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.text[::10]