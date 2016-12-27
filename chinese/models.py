from __future__ import unicode_literals

from django.db import models


class Ideograph(models.Model):
    text = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=20, null=True)
    pinyin_no_accent = models.CharField(max_length=20, null=True)
    image = models.CharField(max_length=50, null=True)
    audio = models.CharField(max_length=50, null=True)
    meaning = models.CharField(max_length=100)
    invented_meaning = models.BooleanField(default=False)
    tone = models.IntegerField(null=True)
    type = models.CharField(max_length=20)


class Story(models.Model):
    text = models.CharField(max_length=1000)
    image = models.CharField(max_length=50, null=True)
    ideograph = models.ForeignKey(Ideograph, on_delete=models.CASCADE)
    position = models.IntegerField()


