from django import forms

class CreateForm(forms.Form):
    Titulo = forms.CharField()
    Carrera = forms.CharField()
    Texto   =   forms.Textarea()
    Link    =   forms.CharField()