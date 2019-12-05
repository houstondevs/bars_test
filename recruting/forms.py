from django import forms
from .models import Recruit, Sith


class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ('name', 'planet', 'age', 'email')


class SithChoiceForm(forms.Form):
    sith = forms.ModelChoiceField(Sith.objects.all(), required=True)