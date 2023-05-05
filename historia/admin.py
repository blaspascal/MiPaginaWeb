from django.contrib import admin
from .models import mifotos, Evento, Participante

from django.utils.html import format_html
from django.utils.safestring import mark_safe
# Register your models here.


class eventoAdmin(admin.ModelAdmin):
    list_display = ("fecha", "orden",  "titulo",
                    "descripcion", "imagen", "foto")
    list_filter = ("fecha",)
    ordering = ("fecha", "orden")
    # search_fields = ("fecha", "titulo", "descripcion")
    date_hierarchy = ("fecha")

#    def imagen(self, obj):
#        fila = "Titulo: " + self.titulo + "- Orden - "+self.orden + " - Descripción " + self.descripcion  + "- imagen -" + format_html('<img scr={} />', obj.imagen.url)
#        return fila

    def foto(self, obj):
        print(obj.imagen.url)
        # return "<img scr=" + obj.imagen.url + "/>"
        return mark_safe("<img scr='" + obj.imagen.url + "' width ='120' />")


admin.site.register(mifotos)
admin.site.register(Evento, eventoAdmin)
admin.site.register(Participante)
