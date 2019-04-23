from django.db import models

# Create your models here.
class Club(models.Model):
    club_name = models.CharField(max_length=100)
    funds = models.IntegerField(default=0)

    def __str__(self):
        return self.club_name

    def get_clubs(self):
        return list(Club.objects.all())

class Calendar(models.Model):
    calendar_name = models.CharField(max_length=100)

    def __str__(self):
        return self.calendar_name

class ChatRoom(models.Model):
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name