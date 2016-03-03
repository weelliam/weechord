from django.db import models


class IntervalType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Interval(models.Model):
    name = models.CharField(max_length=200)
    short = models.CharField(default="", max_length=2)
    unit = models.IntegerField(default=0)
    type = models.ForeignKey(IntervalType, null=True)

    def __str__(self):
        return self.name + "(" + self.short + ")"

class Scale(models.Model):
    name = models.CharField(max_length=200)
    intervals = models.ManyToManyField('Interval', through='ScaleInterval')

    def __str__(self):
        return self.name

    def print_intervals(self):
        return ' | '.join([i.interval.short for i in self.intervals])

class Mode(models.Model):
    name = models.CharField(max_length=200)
    intervals = models.ManyToManyField('Interval', through='ModeInterval')

    def __str__(self):
        return self.name

    def print_intervals(self):
        intervals = ModeInterval.objects.filter(mode=self).order_by('position')
        return ' | '.join([i.interval.short for i in intervals])

class ScaleInterval(models.Model):
    scale = models.ForeignKey(Scale)
    interval = models.ForeignKey(Interval)
    position = models.IntegerField()

class ModeInterval(models.Model):
    mode = models.ForeignKey(Mode)
    interval = models.ForeignKey(Interval)
    position = models.IntegerField()

class Note(models.Model):
    name = models.CharField(max_length=5)
    sharp = models.ForeignKey('self',null=True)
    is_sharp = models.BooleanField(default=0)

    def __str__(self):
        if self.is_sharp:
            return (self.name + "/" + self.get_flat_equivalent()).encode('utf-8')
        else:
            return self.name

    def next_note(self):
        return self.sharp

    def get_flat_equivalent(self):
        if self.is_sharp:
            return self.next_note().name + u"\u266D"
        else:
            return False
