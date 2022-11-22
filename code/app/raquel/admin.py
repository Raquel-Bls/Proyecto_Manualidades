from django.contrib import admin
from .models import Comentarios, Manualidades, Curso, Epocas, Herramientas, Impartidor, Dificultad, ComentariosM  # , ComentariosE

# Register your models here.


class ComentarioInline(admin.TabularInline):
    model = Comentarios


class CursoAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioInline
    ]


class ComentarioMInline(admin.TabularInline):
    model = ComentariosM


class ManualAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioMInline
    ]


# class ComentarioEInline(admin.TabularInline):
 #   model = ComentariosE


# class EpocasAdmin(admin.ModelAdmin):
 #   inlines = [
  #      ComentarioEInline
   # ]


admin.site.register(Comentarios)
admin.site.register(ComentariosM)
# admin.site.register(ComentariosE)
admin.site.register(Manualidades, ManualAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Epocas)  # , EpocasAdmin
admin.site.register(Herramientas)
admin.site.register(Impartidor)
admin.site.register(Dificultad)
