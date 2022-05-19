from django.db import models

# Create your models here.
#This is a table; new table requires a new class (new table; new csv)
#If model modified --> python manage.py makemigrations --> python manage.py migrate
#Goes through edits --> if already applied; skips; else migrates it (double-checks for new models; adds them if new found)
class Anime(models.Model):
    anime_id = models.IntegerField(("anime_id"))
    type = models.CharField(("type"), max_length=10)
    title = models.CharField(("title"), max_length=200)
    synopsis = models.CharField(("synopsis"), max_length=99999)
    episodes = models.IntegerField(("episodes"))
    score = models.FloatField(("score"), max_length=3)
    scored_by = models.IntegerField(("scored_by"))
    rank = models.IntegerField(("rank"))
    popularity = models.IntegerField("popularity")
    url = models.CharField("url", max_length=100)