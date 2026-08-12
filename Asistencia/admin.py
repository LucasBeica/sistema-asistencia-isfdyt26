from django.contrib import admin
from .models import Carrera, Anio, Materia, Alumno, Inscripcion, Asistencia, CicloLectivo

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Anio)
class AnioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    ordering = ('nombre',)

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):

    list_display = ('nombre','mostrar_carrera','anio',)
    list_filter = ('anio',)
    ordering = ('anio','nombre',)

    def mostrar_carrera(self, obj):
        return obj.anio.carrera.nombre

    mostrar_carrera.short_description = 'Carrera'

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre')
    search_fields = ('apellido', 'nombre')
    ordering = ('apellido', 'nombre')

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'inscripcion',
        'fecha',
        'estado')

    list_filter = (
        'fecha',
        'estado',
        'inscripcion__materia',
        'inscripcion__ciclo_lectivo')

    search_fields = (
        'inscripcion__alumno__apellido',
        'inscripcion__alumno__nombre',
        'inscripcion__alumno__dni',)

@admin.register(CicloLectivo)
class CicloLectivoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)
@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = (
        'alumno',
        'materia',
        'ciclo_lectivo',
    )

    list_filter = (
        'ciclo_lectivo',
        'materia',
    )

    search_fields = (
        'alumno__apellido',
        'alumno__nombre',
    )

    ordering = (
        'ciclo_lectivo',
        'materia',
        'alumno__apellido',
    )