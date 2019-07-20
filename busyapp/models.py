from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User,Group

class CompanyInfo(models.Model):
    company = models.OneToOneField(Group,on_delete=models.CASCADE)
    company_username = models.CharField(max_length=264)

    def get_absolute_url(self):
        return reverse('base')

    def __str__(self):
        return self.company_name

class UserInfo(models.Model):
    # company = models.ForeignKey(CompanyInfo, related_name='userinfos', on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('base')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    # userinfo = models.ForeignKey(UserInfo, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=264,unique=True)
    text = models.TextField()
    image = models.ImageField(upload_to="post_images")
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)
    slug = models.SlugField(default='',blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approve_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('busyapp.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=264)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text