from django import forms
from .models import tarea

class TareaForm(forms.ModelForm):#Se puede asociar el form a un modelo, y se puede usar el save()
    class Meta:#una clase meta le dice a la clase como comportarse
        model = tarea
        fields = ['tarea']