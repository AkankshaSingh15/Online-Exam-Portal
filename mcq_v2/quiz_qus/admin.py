from django.contrib import admin

from .models import *
# Register your models here.


admin.site.register(question)
admin.site.register(subQuestion)

# class questionAdmin(admin.ModelAdmin):
#   List_display = ( "qus_id", "title","desc")

# admin.site.register(question, questionAdmin)