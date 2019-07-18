from django.contrib import admin
from busyapp import models

# Register your models here.
admin.site.register(models.CompanyInfo)
admin.site.register(models.Comment)
admin.site.register(models.Post)
admin.site.register(models.UserInfo)