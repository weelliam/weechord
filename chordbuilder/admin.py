from django.contrib import admin

from .models import Note
from .models import Scale
from .models import IntervalType
from .models import Interval
from .models import Mode
from .models import ScaleInterval
from .models import ModeInterval

class IntervalAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'short', 'unit')

class ModeIntervalInline(admin.TabularInline):
    model = ModeInterval
    extra = 7

class ModeAdmin(admin.ModelAdmin):
    inlines = [ModeIntervalInline]

class ModeIntervalAdmin(admin.ModelAdmin):
    list_display = ('mode', 'interval', 'position')


class ScaleIntervalInline(admin.TabularInline):
    model = ScaleInterval
    extra = 7

class ScaleAdmin(admin.ModelAdmin):
    inlines = [ScaleIntervalInline]

class ScaleIntervalAdmin(admin.ModelAdmin):
    list_display = ('scale', 'interval', 'position')

admin.site.register(Note)
admin.site.register(Scale, ScaleAdmin)
admin.site.register(IntervalType)
admin.site.register(Interval, IntervalAdmin)
admin.site.register(Mode, ModeAdmin)
admin.site.register(ScaleInterval, ScaleIntervalAdmin)
admin.site.register(ModeInterval, ModeIntervalAdmin)