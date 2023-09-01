from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'  # O puedes especificar los campos que deseas mostrar en el formulario
