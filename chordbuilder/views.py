from django.shortcuts import render

from .models import Note


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def notes(request):
    all_note_list = Note.objects.order_by('name')
    context = {'all_note_list': all_note_list}

    return render(request, 'chordbuilder/notes.html', context)
