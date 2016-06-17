from django.shortcuts import render
from django.db.models import Q

from .models import Note
from .models import Mode
from .models import Scale
from .models import Interval
from .models import IntervalType

from .forms import ScaleBuild

def index(request):
    return render(request, 'chordbuilder/index.html')

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

def build(request):
    all_note_list = Note.objects.order_by('name')
    context = {'all_note_list': all_note_list}

    return render(request, 'chordbuilder/build.html', context)

def get_scale(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScaleBuild(request.POST)
        # check whether it's valid:
        if form.is_valid():
            root = form.cleaned_data['root_note']
            chords = {}

            all_scale_list = Scale.objects.order_by('name')

            for scale in all_scale_list:
                current_note = root
                chord = []
                chord.append(current_note)
                print "scale: {}".format(scale.name)
                for interval in scale.intervals.all():
                    print "interval of: {}".format(interval.unit)
                    for i in range(0,interval.unit):
                        current_note = current_note.next_note()
                        print "current_note: {}".format(current_note)
                    print "add: {}".format(current_note)
                    chord.append(current_note)

                chords[scale.name] = chord

            context = {'chords': chords}

            return render(request, 'chordbuilder/scale.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScaleBuild()

    return render(request, 'chordbuilder/build.html', {'form': form})