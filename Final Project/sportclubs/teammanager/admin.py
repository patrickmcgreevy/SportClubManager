from django.contrib import admin
from .models import Club

# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    fields = ['club_name', 'funds']


admin.site.register(Club, ClubAdmin)