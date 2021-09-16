from django.contrib import admin
from . import models

# Register your models here.


# 이 모델을 장고에 연걸해야함
@admin.register(models.User)  # 어드민 패널에서 이 user을 보고 싶다는 말
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("superhost", "language", "currency")
