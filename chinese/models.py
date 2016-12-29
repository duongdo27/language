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


class Example(models.Model):
    ideograph = models.ForeignKey(Ideograph, on_delete=models.CASCADE)
    position = models.IntegerField()
    word = models.CharField(max_length=50, null=True)
    word_meaning = models.CharField(max_length=100, null=True)
    word_pinyin = models.CharField(max_length=100, null=True)
    word_audio = models.CharField(max_length=50,null=True)
    phrase = models.CharField(max_length=100, null=True)
    phrase_meaning = models.CharField(max_length=200, null=True)
    phrase_pinyin = models.CharField(max_length=200, null=True)
    phrase_audio = models.CharField(max_length=50,null=True)


class Component(models.Model):
    ideograph = models.ForeignKey(Ideograph, on_delete=models.CASCADE, related_name='ideograph')
    component = models.ForeignKey(Ideograph, on_delete=models.CASCADE, related_name='component')


class Deck(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.IntegerField()
    image = models.CharField(max_length=50, null=True)


class DeckIdeograph(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    ideograph = models.ForeignKey(Ideograph, on_delete=models.CASCADE)
    lesson = models.IntegerField()
    position = models.IntegerField()
