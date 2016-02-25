from django.db import models


#class ChordPattern(models.Model):
#    name = models.CharField(max_length=200)

#class Chord(models.Model):
#    pattern = models.ForeignKey(ChordPattern)
#    scale = models.ForeignKey(Scale)
#    notes = models.ManyToManyField(Note)

class Scale(models.Model):
    name = models.CharField(max_length=200)

class Interval(models.Model):
    name = models.CharField(max_length=200)
    unit = models.IntegerField(default=0)

class Note(models.Model):
    name = models.CharField(max_length=5)
    sharp = models.ForeignKey('self',null=True)
    is_sharp = models.BooleanField(default=0)

    def __str__(self):
        if self.is_sharp:
            return self.name + "/" + self.get_flat_equivalent()
        else:
            return self.name

    def next_note(self):
        return self.sharp

    def get_flat_equivalent(self):
        if self.is_sharp:
            return self.next_note().name + u"\u266D"
        else:
            return False
