from django.contrib import admin
from . import models

# Register your models here.


# 이 모델을 장고에 연걸해야함
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    bio = models.TextField()
