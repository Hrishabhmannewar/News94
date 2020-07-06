from django.db import models
import datetime


# Create your models here.
class newsupdate(models.Model):
    news_id = models.AutoField
    news_head = models.CharField(max_length=80)
    desc = models.CharField(max_length=2500)
    image = models.ImageField(upload_to='news/images')
    date = models.DateTimeField(default= datetime.datetime.now,blank=True)
    only_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.news_head


class Feedback(models.Model):
    feedb_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , default="")
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=150, default="")
    message = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.email



