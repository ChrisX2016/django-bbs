from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(u'title标题',max_length=255,unique=True)
    head_img = models.ImageField(upload_to='uploads')
    summary = models.CharField(max_length=255)
    category = models.ForeignKey('Category',verbose_name=u'category板块')
    content = models.TextField(u'content')
    author = models.ForeignKey('UserProfile')
    publish_date = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=True)
    priority = models.IntegerField(u'priority', default=1000)

    def __str__(self):
        return '<%s>, author:%s>' % (self.title, self.author)


class Comment(models.Model):
    article = models.ForeignKey('Article')
    user = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=1000)
    parent_comment = models.ForeignKey('self', related_name='p_comment', blank=True, null=True)

    def __str__(self):
        return '<%s, user:%s>' % (self.comment, self.user)


class ThumbUp(models.Model):
    article = models.ForeignKey('Article')
    user = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<user:%s>' % self.user


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    groups = models.ManyToManyField('UserGroup')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    admin = models.ManyToManyField('UserProfile')

    def __str__(self):
        return self.name


class UserGroup(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name
