from django.db import models

# Create your models here.
class Conference(models.Model):
    CONFERENCE_CHOICES = [
        ("W", "West"),
        ("E", "East")
    ]
    name = models.CharField(
        max_length=4, choices=CONFERENCE_CHOICES, blank=True
    )

class Division(models.Model):
    DIVISION_CHOICES = [
        ("AT", "Atlantic"),
        ("CE", "Central"),
        ("SE", "Southeast"),
        ("NW", "Northwest"),
        ("PA", "Pacific"),
        ("SW", "Southwest")
    ]

    name = models.CharField(max_length=10, choices=DIVISION_CHOICES, blank=True)
    conf = models.ForeignKey(
        Conference, on_delete=models.PROTECT, related_name="divisions"
    )


class Team(models.Model):
    city = models.CharField(max_length=64)
    fullName = models.CharField(max_length=64)
    teamId = models.IntegerField()
    nickname = models.CharField(max_length=64)
    logo = models.URLField()
    shortName = models.CharField(max_length=10)
    allStar = models.IntegerField()
    conf = models.ForeignKey(
        Conference, on_delete=models.PROTECT, related_name="teams"
    )
    div = models.ForeignKey(
        Division, on_delete=models.PROTECT, related_name="teams"
    )
    

    def __str__(self):
        return f"{self.teamId}: {self.fullName}"

# class Question(models.Model):
    