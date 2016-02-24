from django.db import models


#class ChordPattern(models.Model):
#    name = models.CharField(max_length=200)

#class Chord(models.Model):
#    pattern = models.ForeignKey(ChordPattern)
#    scale = models.ForeignKey(Scale)
#    notes = models.ManyToManyField(Note)

#class Scale(models.Model):
#    name = models.CharField(max_length=200)
#    notes = models.ManyToManyField(Note)

class Note(models.Model):
    name = models.CharField(max_length=5)
    sharp = models.ForeignKey('self',null=True)
    is_sharp = models.BooleanField(default=0)

    def __str__(self):
        return self.name

    def next_note(self):
        return self.sharp
