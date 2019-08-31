from django.db import models
from django.utils import timezone
from django.urls import reverse
from busyboss import settings
from django.contrib.auth.models import User,Group

class CompanyInfo(models.Model):
    company = models.OneToOneField(Group,on_delete=models.CASCADE)
    company_username = models.CharField(max_length=264)

    def get_absolute_url(self):
        return reverse('base')

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('base')

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    title = models.CharField(max_length=264,unique=True)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now(),blank=True)
    published_date = models.DateTimeField(blank=True,null=True)
    slug = models.SlugField(default='',blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('busyapp:post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('busyapp.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('busyapp:post_list')

    def __str__(self):
        return self.text