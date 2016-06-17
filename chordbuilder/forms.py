from django import forms

from .models import Note

class ScaleBuild(forms.Form):
	root_note = forms.ModelChoiceField(queryset=Note.objects.order_by('name'))