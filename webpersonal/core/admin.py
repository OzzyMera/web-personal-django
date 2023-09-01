from django.contrib import admin
from .models import Contacto 
# Register your models here.
 # Importa el modelo que has definido en models.py

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_contacto')  # Campos que se mostrarán en la lista de registros
    list_filter = ('opciones', 'contacto_preferido')  # Filtros en el panel de administración
    search_fields = ('nombre', 'email', 'telefono', 'propiedad')  # Búsqueda por estos campos
