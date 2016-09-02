from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    user = models.ForeignKey(User,
                             related_name='detail',
                             on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    avatar = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Link(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    image = models.CharField(max_length=500, blank=True)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.url


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class UserLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    is_read = models.BooleanField()
    is_favorite = models.BooleanField()
    is_public = models.BooleanField()
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "{}'s {}".format(self.user.username, self.link.title)


class LinkComment(models.Model):
    target = models.ForeignKey(UserLink, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date_created = models.DateTimeField()

    def __str__(self):
        return "{}'s comment on {}".format(self.author.username,
                                           self.target.link.title)
