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


class Category(models.Model):
    # link = models.ForeignKey(Link, on_delete=models.CASCADE)
    # link = models.ForeignKey(Link, on_delete=models.CASCADE)


class UserLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    was_seen = models.BooleanField()
    is_favorite = models.BooleanField()


#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
#
#     def __str__(self):
#         return self.question_text
