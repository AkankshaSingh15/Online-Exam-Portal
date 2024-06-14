from django.contrib import admin
from .models import leaderboard

# Register your models here.


# admin.site.register(leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
  list_display = ("id", "user", "correct_qus","wrong_qus","points","message","attempted_qus")
  
admin.site.register(leaderboard, LeaderboardAdmin)
