from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetail(models.Model):
    bio = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)


class Link(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    date_created = models.DateTimeField()


class UserLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    was_seen = models.BooleanField()
    is_favorite = models.BooleanField()
    is_public = models.BooleanField()


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)


class LinkCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)


class LinkTag(models.Model):
    link = models.ForeignKey(UserLink, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class LinkComment(models.Model):
    target = models.ForeignKey(UserLink, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date_created = models.DateTimeField()
