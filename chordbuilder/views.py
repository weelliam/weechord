from django.shortcuts import render
from django.db.models import Q

from .models import Note
from .models import Mode
from .models import Scale
from .models import Interval
from .models import IntervalType


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def modes(request):
    all_mode_list = Mode.objects.order_by('name')
    context = {'all_mode_list': all_mode_list}

    return render(request, 'chordbuilder/modes.html', context)

def scales(request):
    all_scale_list = Scale.objects.order_by('name')
    context = {'all_scale_list': all_scale_list}

    return render(request, 'chordbuilder/scales.html', context)

def notes(request):
    all_note_list = Note.objects.order_by('name')
    context = {'all_note_list': all_note_list}

    return render(request, 'chordbuilder/notes.html', context)

def intervals(request):
    units = range(0,12)
    types = IntervalType.objects.order_by('name')

    headers = list()
    for type in types:
        headers.append(type.name)

    rows = list()
    for unit in units:
        columns = list()
        for type in types:
            intervals = Interval.objects.filter(unit=unit).filter(type=type)
            column = ""
            for interval in intervals:
                column = column + interval.name + " [ " + interval.short + " ] " + " "
            columns.append(column)
        rows.append(columns)

    context = {
        'headers': headers,
        'rows': rows
    }

    return render(request, 'chordbuilder/intervals.html', context)