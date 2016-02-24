from django.db import models


class ChordPattern(models.Model):
    name = models.CharField(max_length=200)

class Chord(models.Model):
    scale = models.ForeignKey(ChordPattern)
    scale = models.ForeignKey(Scale)
#    notes = models.ManyToManyField(Note)

class Scale(models.Model):
    name = models.CharField(max_length=200)
    notes = models.ManyToManyField(Note)

class Note(models.Model):
    name = models.CharField(max_length=1)

class MidNote(models.Model):
    sharpNote = models.ForeignKey(Note)
    flatNote = models.ForeignKey(Note)
