from django.contrib import admin
from .models import quizze
# Register your models here.

admin.site.register(quizze)
# class quizzeAdmin(admin.ModelAdmin):
#   list_display = ("id", "title", "time","ques")
  
# admin.site.register(quizze,quizzeAdmin)