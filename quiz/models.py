from django.db import models

# Create your models here.
class Conference(models.Model):
    CONFERENCE_CHOICES = [
        ("west", "West"),
        ("east", "East")
    ]
    name = models.CharField(
        max_length=64, choices=CONFERENCE_CHOICES
    )

    def __str__(self):
        return f"{self.name}"

class Division(models.Model):
    DIVISION_CHOICES = [
        ("atlantic", "Atlantic"),
        ("central", "Central"),
        ("southeast", "Southeast"),
        ("northwest", "Northwest"),
        ("pacific", "Pacific"),
        ("southwest", "Southwest")
    ]

    name = models.CharField(max_length=64, choices=DIVISION_CHOICES)
    conf = models.ForeignKey(
        Conference, on_delete=models.PROTECT, related_name="divisions"
    )

    def __str__(self):
        return f"{self.name}"


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
    