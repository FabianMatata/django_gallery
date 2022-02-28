from django.db import models
from django.contrib.auth.models import User
# from sqlalchemy import null

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

        
class Location(models.Model):
    name = models.CharField(max_length =50)

    @classmethod
    def tag_articles(cls):
        tags = cls.objects.all()
        return tags

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def update_location(self,update):
        self.name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate

    def __str__(self):
        return self.name


class Location(models.Model):
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Location'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    # location = models.CharField(max_length=200)
    # location = models.Location(max_length=200)
    location = models.TextField(null=True, blank=True)
    # location = models.CharField(max_length=100)
    # image_location = models.ForeignKey('Location', on_delete=models.SET_NULL)
    description = models.TextField()

def __str__(self):
    return self.description