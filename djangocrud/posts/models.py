from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, null=False)
    body = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    @property
    def author(self):
        return self.user_set.all()

    def __str__(self):
        return self.title


class Catagory(models.Model):
    name = models.TextField(null=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class PostCatagory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['catagory']

    def __str__(self):
        return self.catagory


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['tag']

    def __str__(self):
        return self.tag
