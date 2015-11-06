from django import forms

class PaisForm(forms.Form):
    pais = forms.CharField(label='pais', max_length=100)
