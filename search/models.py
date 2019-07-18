from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):

    title = models.CharField(max_length=264)
    text = models.TextField()
    image = models.ImageField(upload_to="post_images")
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    slug = models.SlugField(default='',blank=True)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()
    
    def __str__(self):
        return self.title