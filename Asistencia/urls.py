from django.urls import path
from . import views


urlpatterns = [

# ==================================================
# INICIO
# ==================================================

    path(
        '',
        views.inicio,
        name='inicio'
    ),


# ==================================================
# CARRERAS
# ==================================================

    path(
        'carreras/',
        views.lista_carreras,
        name='lista_carreras'
    ),

    path(
        'carreras/nueva/',
        views.nueva_carrera,
        name='nueva_carrera'
    ),

    path(
        'carreras/<int:id>/editar/',
        views.editar_carrera,
        name='editar_carrera'
    ),

    path(
        'carreras/<int:id>/eliminar/',
        views.eliminar_carrera,
        name='eliminar_carrera'
    ),


# ==================================================
# CICLOS LECTIVOS
# ==================================================

    path(
        'ciclos/',
        views.lista_ciclos,
        name='lista_ciclos'
    ),

    path(
        'ciclos/nuevo/',
        views.nuevo_ciclo,
        name='nuevo_ciclo'
    ),

    path(
        'ciclos/<int:id>/editar/',
        views.editar_ciclo,
        name='editar_ciclo'
    ),

    path(
        'ciclos/<int:id>/eliminar/',
        views.eliminar_ciclo,
        name='eliminar_ciclo'
    ),

# ==================================================
# AÑOS
# ==================================================

    path(
    'carreras/<int:carrera_id>/anios/',
    views.lista_anios,
    name='lista_anios'
),

    path(
    'carreras/<int:carrera_id>/anios/nuevo/',
    views.nuevo_anio,
    name='nuevo_anio'
),

    path(
    'anios/<int:id>/editar/',
    views.editar_anio,
    name='editar_anio'
),

    path(
    'anios/<int:id>/eliminar/',
    views.eliminar_anio,
    name='eliminar_anio'
),

# ==================================================
# MATERIAS
# ==================================================

    path(
        'anios/<int:anio_id>/materias/',
        views.lista_materias,
        name='lista_materias'
    ),

    path(
        'anios/<int:anio_id>/materias/nueva/',
        views.nueva_materia,
        name='nueva_materia'
    ),

    path(
        'materias/<int:id>/editar/',
        views.editar_materia,
        name='editar_materia'
    ),

    path(
        'materias/<int:id>/eliminar/',
        views.eliminar_materia,
        name='eliminar_materia'
    ),

# ==================================================
# ALUMNOS
# ==================================================

path(
    'alumnos/',
    views.lista_alumnos,
    name='lista_alumnos'
),

path(
    'alumnos/nuevo/',
    views.nuevo_alumno,
    name='nuevo_alumno'
),

path(
    'alumnos/<int:id>/editar/',
    views.editar_alumno,
    name='editar_alumno'
),

path(
    'alumnos/<int:alumno_id>/eliminar/',
    views.eliminar_alumno,
    name='eliminar_alumno'
),

path(
    'alumnos/<int:alumno_id>/inscribir/',
    views.inscribir_alumno,
    name='inscribir_alumno'
),

# ==================================================
# ASISTENCIA
# ==================================================

    path(
        'asistencia/',
        views.seleccionar_asistencia,
        name='seleccionar_asistencia'
    ),

# ==================================================
# REPORTES
# ==================================================

path(
    'reportes/asistencia/',
    views.reporte_asistencia,
    name='reporte_asistencia'
),
path(
    'asistencia/buscar-alumno/',
    views.buscar_alumno_asistencia,
    name='buscar_alumno_asistencia'
),
# ==================================================
# buscador
# ==================================================
path(
    'buscador/',
    views.buscar_alumno_asistencia,
    name='buscar_alumno_asistencia'
),

]