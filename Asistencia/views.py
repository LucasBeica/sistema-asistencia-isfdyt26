from datetime import date
from django.db.models import Q
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import ( Carrera, CicloLectivo, Anio, Materia, Alumno, Inscripcion, Asistencia)

from .forms import ( CarreraForm, CicloLectivoForm, AnioForm, MateriaForm, AlumnoForm)

from datetime import date
# ==================================================
# INICIO
# ==================================================

def inicio(request):

    return render(
        request,
        'asistencia/inicio.html'
    )


# ==================================================
# CARRERAS
# ==================================================

def lista_carreras(request):

    carreras = Carrera.objects.all().order_by(
        'nombre'
    )

    return render(
        request,
        'asistencia/carreras/lista.html',
        {
            'carreras': carreras
        }
    )


def nueva_carrera(request):

    if request.method == 'POST':

        formulario = CarreraForm(
            request.POST
        )

        if formulario.is_valid():

            formulario.save()

            return redirect(
                'lista_carreras'
            )

    else:

        formulario = CarreraForm()

    return render(
        request,
        'asistencia/carreras/formulario.html',
        {
            'formulario': formulario
        }
    )


def editar_carrera(request, id):

    carrera = get_object_or_404(
        Carrera,
        id=id
    )

    if request.method == 'POST':

        formulario = CarreraForm(
            request.POST,
            instance=carrera
        )

        if formulario.is_valid():

            formulario.save()

            return redirect(
                'lista_carreras'
            )

    else:

        formulario = CarreraForm(
            instance=carrera
        )

    return render(
        request,
        'asistencia/carreras/formulario.html',
        {
            'formulario': formulario,
            'carrera': carrera
        }
    )


def eliminar_carrera(request, id):

    carrera = get_object_or_404(
        Carrera,
        id=id
    )

    if request.method == 'POST':

        carrera.delete()

        return redirect(
            'lista_carreras'
        )

    return render(
        request,
        'asistencia/carreras/eliminar.html',
        {
            'carrera': carrera
        }
    )


# ==================================================
# CICLOS LECTIVOS
# ==================================================

def lista_ciclos(request):

    ciclos = CicloLectivo.objects.all().order_by(
        '-nombre'
    )

    return render(
        request,
        'asistencia/lista_ciclos.html',
        {
            'ciclos': ciclos
        }
    )


def nuevo_ciclo(request):

    if request.method == 'POST':

        formulario = CicloLectivoForm(
            request.POST
        )

        if formulario.is_valid():

            formulario.save()

            return redirect(
                'lista_ciclos'
            )

    else:

        formulario = CicloLectivoForm()

    return render(
        request,
        'asistencia/ciclos/formulario.html',
        {
            'formulario': formulario
        }
    )


def editar_ciclo(request, id):

    ciclo = get_object_or_404(
        CicloLectivo,
        id=id
    )

    if request.method == 'POST':

        formulario = CicloLectivoForm(
            request.POST,
            instance=ciclo
        )

        if formulario.is_valid():

            formulario.save()

            return redirect(
                'lista_ciclos'
            )

    else:

        formulario = CicloLectivoForm(
            instance=ciclo
        )

    return render(
        request,
        'asistencia/ciclos/formulario.html',
        {
            'formulario': formulario,
            'ciclo': ciclo
        }
    )


def eliminar_ciclo(request, id):

    ciclo = get_object_or_404(
        CicloLectivo,
        id=id
    )

    if request.method == 'POST':

        ciclo.delete()

        return redirect(
            'lista_ciclos'
        )

    return render(
        request,
        'asistencia/ciclos/eliminar.html',
        {
            'ciclo': ciclo
        }
    )


# ==================================================
# AÑOS
# Cada año pertenece a una carrera.
# ==================================================

def lista_anios(request, carrera_id):

    carrera = get_object_or_404(
        Carrera,
        id=carrera_id
    )

    anios = carrera.anios.all().order_by(
        'nombre'
    )

    return render(
        request,
        'asistencia/anios/lista.html',
        {
            'carrera': carrera,
            'anios': anios
        }
    )


def nuevo_anio(request, carrera_id):

    carrera = get_object_or_404(
        Carrera,
        id=carrera_id
    )

    if request.method == 'POST':

        formulario = AnioForm(
            request.POST
        )

        if formulario.is_valid():

            anio = formulario.save(
                commit=False
            )

            anio.carrera = carrera

            anio.save()

            return redirect(
                'lista_anios',
                carrera_id=carrera.id
            )

    else:

        formulario = AnioForm()

    return render(
        request,
        'asistencia/anios/formulario.html',
        {
            'formulario': formulario,
            'carrera': carrera
        }
    )


def editar_anio(request, id):

    anio = get_object_or_404(
        Anio,
        id=id
    )

    if request.method == 'POST':

        formulario = AnioForm(
            request.POST,
            instance=anio
        )

        if formulario.is_valid():

            formulario.save()

            return redirect(
                'lista_anios',
                carrera_id=anio.carrera.id
            )

    else:

        formulario = AnioForm(
            instance=anio
        )

    return render(
        request,
        'asistencia/anios/formulario.html',
        {
            'formulario': formulario,
            'anio': anio,
            'carrera': anio.carrera
        }
    )


def eliminar_anio(request, id):

    anio = get_object_or_404(
        Anio,
        id=id
    )

    carrera_id = anio.carrera.id

    if request.method == 'POST':

        anio.delete()

        return redirect(
            'lista_anios',
            carrera_id=carrera_id
        )

    return render(
        request,
        'asistencia/anios/eliminar.html',
        {
            'anio': anio,
            'carrera': anio.carrera
        }
    )


# ==================================================
# MATERIAS
# Cada materia pertenece a un año.
# ==================================================

def lista_materias(request, anio_id):

    anio = get_object_or_404(
        Anio,
        id=anio_id
    )

    materias = anio.materias.all().order_by(
        'nombre'
    )

    return render(
        request,
        'asistencia/materias/lista.html',
        {
            'anio': anio,
            'materias': materias
        }
    )


def nueva_materia(request, anio_id):

    anio = get_object_or_404(
        Anio,
        id=anio_id
    )

    if request.method == 'POST':

        formulario = MateriaForm(
            request.POST
        )

        if formulario.is_valid():

            materia = formulario.save(
                commit=False
            )

            materia.anio = anio

            materia.save()

            return redirect(
                'lista_materias',
                anio_id=anio.id
            )

    else:

        formulario = MateriaForm()

    return render(
        request,
        'asistencia/materias/formulario.html',
        {
            'formulario': formulario,
            'anio': anio
        }
    )


def editar_materia(request, id):

    materia = get_object_or_404(
        Materia,
        id=id
    )

    if request.method == 'POST':

        formulario = MateriaForm(
            request.POST,
            instance=materia
        )

        if formulario.is_valid():

            formulario.save()

            return redirect(
                'lista_materias',
                anio_id=materia.anio.id
            )

    else:

        formulario = MateriaForm(
            instance=materia
        )

    return render(
        request,
        'asistencia/materias/formulario.html',
        {
            'formulario': formulario,
            'materia': materia,
            'anio': materia.anio
        }
    )


def eliminar_materia(request, id):

    materia = get_object_or_404(
        Materia,
        id=id
    )

    anio_id = materia.anio.id

    if request.method == 'POST':

        materia.delete()

        return redirect(
            'lista_materias',
            anio_id=anio_id
        )

    return render(
        request,
        'asistencia/materias/eliminar.html',
        {
            'materia': materia,
            'anio': materia.anio
        }
    )

# ==================================================
# ALUMNOS
# ==================================================

def lista_alumnos(request):

    buscar = request.GET.get('buscar', '').strip()

    alumnos = Alumno.objects.all().select_related(
        'carrera',
    ).order_by(
        'apellido',
        'nombre'
    )

    # ==================================================
    # BUSCADOR
    # ==================================================

    if buscar:

        alumnos = alumnos.filter(
            Q(nombre__icontains=buscar) |
            Q(apellido__icontains=buscar) |
            Q(dni__icontains=buscar)
        )

    return render(
        request,
        'asistencia/alumno/lista.html',
        {
            'alumnos': alumnos,
            'buscar': buscar,
        }
    )

def nuevo_alumno(request):

    if request.method == 'POST':

        formulario = AlumnoForm(
            request.POST
        )

        if formulario.is_valid():

            alumno = formulario.save()

            return redirect(
                'lista_alumnos'
            )

    else:

        formulario = AlumnoForm()

    return render(
        request,
        'asistencia/alumno/formulario.html',
        {
            'formulario': formulario
        }
    )


def editar_alumno(request, id):

    alumno = get_object_or_404(
        Alumno,
        id=id
    )

    if request.method == 'POST':

        formulario = AlumnoForm(
            request.POST,
            instance=alumno
        )

        if formulario.is_valid():

            formulario.save()

            return redirect(
                'lista_alumnos'
            )

    else:

        formulario = AlumnoForm(
            instance=alumno
        )

    return render(
        request,
        'asistencia/alumno/formulario.html',
        {
            'formulario': formulario,
            'alumno': alumno
        }
    )


def eliminar_alumno(request, alumno_id):

    alumno = get_object_or_404(
        Alumno,
        id=alumno_id
    )

    if request.method == 'POST':

        alumno.delete()

        return redirect(
            'lista_alumnos'
        )

    return render(
        request,
        'asistencia/alumno/eliminar.html',
        {
            'alumno': alumno
        }
    )

# ==================================================
# INSCRIPCIONES
#
# Un alumno puede cursar materias de diferentes años.
# ==================================================

def inscribir_alumno(request, alumno_id):

    alumno = get_object_or_404(
        Alumno,
        id=alumno_id
    )

    # Todas las materias de la carrera del alumno
    materias = Materia.objects.filter(
        anio__carrera=alumno.carrera
    ).select_related(
        'anio'
    ).order_by(
        'anio__nombre',
        'nombre'
    )

    # Materias que ya tiene seleccionadas
    materias_inscriptas = set(
        Inscripcion.objects.filter(
            alumno=alumno
        ).values_list(
            'materia_id',
            flat=True
        )
    )

    if request.method == 'POST':

        materias_seleccionadas = request.POST.getlist(
            'materias'
        )

        # ------------------------------------------
        # ELIMINAR LAS QUE SE DESELECCIONARON
        # ------------------------------------------

        Inscripcion.objects.filter(
            alumno=alumno
        ).exclude(
            materia_id__in=materias_seleccionadas
        ).delete()

        # ------------------------------------------
        # CREAR LAS NUEVAS INSCRIPCIONES
        # ------------------------------------------

        for materia_id in materias_seleccionadas:

            materia = get_object_or_404(
                Materia,
                id=materia_id,
                anio__carrera=alumno.carrera
            )

            Inscripcion.objects.get_or_create(
                alumno=alumno,
                materia=materia,
                ciclo_lectivo=alumno.carrera.ciclo_lectivo
            )

        return redirect(
            'lista_alumnos'
        )

    return render(
        request,
        'asistencia/alumno/inscribir.html',
        {
            'alumno': alumno,
            'materias': materias,
            'materias_inscriptas': materias_inscriptas
        }
    )

# ==================================================
# TOMAR ASISTENCIA
# ==================================================

def seleccionar_asistencia(request):

    # ==================================================
    # DATOS DE LOS FILTROS
    # ==================================================

    ciclo_id = request.GET.get('ciclo')
    carrera_id = request.GET.get('carrera')
    anio_id = request.GET.get('anio')
    materia_id = request.GET.get('materia')
    buscar = request.GET.get('buscar', '').strip()

    ciclos = CicloLectivo.objects.all().order_by(
        '-nombre'
    )

    carreras = Carrera.objects.none()
    anios = Anio.objects.none()
    materias = Materia.objects.none()

    # ==================================================
    # CARRERAS
    # ==================================================

    if ciclo_id:

        carreras = Carrera.objects.filter(
            ciclo_lectivo_id=ciclo_id
        ).order_by(
            'nombre'
        )

    # ==================================================
    # AÑOS
    # ==================================================

    if carrera_id:

        anios = Anio.objects.filter(
            carrera_id=carrera_id
        ).order_by(
            'nombre'
        )

    # ==================================================
    # MATERIAS
    # ==================================================

    if anio_id:

        materias = Materia.objects.filter(
            anio_id=anio_id
        ).order_by(
            'nombre'
        )

    # ==================================================
    # FECHA
    # ==================================================

    fecha = date.today()

    if not fecha:

        fecha = date.today().isoformat()

    # ==================================================
    # GUARDAR ASISTENCIA
    # ==================================================

    if request.method == 'POST':

        ciclo_id = request.POST.get('ciclo')
        carrera_id = request.POST.get('carrera')
        anio_id = request.POST.get('anio')
        materia_id = request.POST.get('materia')
        fecha = date.today()

        materia = get_object_or_404(
            Materia,
            id=materia_id,
            anio_id=anio_id,
            anio__carrera_id=carrera_id,
            anio__carrera__ciclo_lectivo_id=ciclo_id
        )

        inscripciones = Inscripcion.objects.filter(
            materia=materia,
            ciclo_lectivo_id=ciclo_id
        )

        # ------------------------------------------
        # GUARDAR ESTADO DE CADA ALUMNO
        # ------------------------------------------

        for inscripcion in inscripciones:

            estado = request.POST.get(
                f'estado_{inscripcion.id}',
                'P'
            )

            Asistencia.objects.update_or_create(

                inscripcion=inscripcion,

                fecha=fecha,

                defaults={
                    'estado': estado
                }
            )

        # ------------------------------------------
        # VOLVER A LA MISMA PANTALLA
        # ------------------------------------------

        return redirect(
            f'/asistencia/?'
            f'ciclo={ciclo_id}&'
            f'carrera={carrera_id}&'
            f'anio={anio_id}&'
            f'materia={materia_id}&'
            f'fecha={fecha}'
        )

    # ==================================================
    # ALUMNOS INSCRIPTOS
    # ==================================================

    alumnos = []

    materia_seleccionada = None

    if materia_id and ciclo_id:

        materia_seleccionada = get_object_or_404(
            Materia,
            id=materia_id,
            anio_id=anio_id,
            anio__carrera_id=carrera_id,
            anio__carrera__ciclo_lectivo_id=ciclo_id
        )

        inscripciones = Inscripcion.objects.filter(
            materia=materia_seleccionada,
            ciclo_lectivo_id=ciclo_id
        ).select_related(
            'alumno'
        ).order_by(
            'alumno__apellido',
            'alumno__nombre'
        )

        # ==================================================
        # ASISTENCIAS DE ESA FECHA
        # ==================================================

        asistencias = Asistencia.objects.filter(
            inscripcion__in=inscripciones,
            fecha=fecha
        )

        estados = {
            asistencia.inscripcion_id:
                asistencia.estado
            for asistencia in asistencias
        }

        # ==================================================
        # AGREGAR ESTADO ACTUAL
        # ==================================================

        for inscripcion in inscripciones:

            inscripcion.estado_actual = estados.get(
                inscripcion.id,
                'P'
            )

            alumnos.append(
                inscripcion
            )

    # ==================================================
    # MOSTRAR PANTALLA
    # ==================================================

    return render(
        request,
        'asistencia/asistencia/seleccionar.html',
        {
            'ciclos': ciclos,
            'carreras': carreras,
            'anios': anios,
            'materias': materias,

            'alumnos': alumnos,

            'materia_seleccionada':
                materia_seleccionada,

            'ciclo_id': ciclo_id,
            'carrera_id': carrera_id,
            'anio_id': anio_id,
            'materia_id': materia_id,

            'fecha': fecha,
        }
    )

# ==================================================
# REPORTES DE ASISTENCIA
# ==================================================

def reporte_asistencia(request):

    # ==================================================
    # DATOS DE LOS FILTROS
    # ==================================================

    ciclo_id = request.GET.get('ciclo')
    carrera_id = request.GET.get('carrera')
    anio_id = request.GET.get('anio')
    materia_id = request.GET.get('materia')

    # ==================================================
    # LISTAS PARA LOS SELECT
    # ==================================================

    ciclos = CicloLectivo.objects.all().order_by('-nombre')

    carreras = Carrera.objects.none()
    anios = Anio.objects.none()
    materias = Materia.objects.none()

    if ciclo_id:

        carreras = Carrera.objects.filter(
            ciclo_lectivo_id=ciclo_id
        ).order_by('nombre')

    if carrera_id:

        anios = Anio.objects.filter(
            carrera_id=carrera_id
        ).order_by('nombre')

    if anio_id:

        materias = Materia.objects.filter(
            anio_id=anio_id
        ).order_by('nombre')

    # ==================================================
    # DATOS DEL REPORTE
    # ==================================================

    alumnos_reporte = []

    materia_seleccionada = None

    if materia_id and ciclo_id and carrera_id and anio_id:

        # Buscamos la materia verificando toda la relación:
        # Ciclo → Carrera → Año → Materia

        materia_seleccionada = Materia.objects.filter(
            id=materia_id,
            anio_id=anio_id,
            anio__carrera_id=carrera_id,
            anio__carrera__ciclo_lectivo_id=ciclo_id
        ).first()

        # ==================================================
        # SI LA MATERIA EXISTE
        # ==================================================

        if materia_seleccionada:

            inscripciones = Inscripcion.objects.filter(
                materia=materia_seleccionada,
                ciclo_lectivo_id=ciclo_id
            ).select_related(
                'alumno'
            ).order_by(
                'alumno__apellido',
                'alumno__nombre'
            )

            for inscripcion in inscripciones:

                asistencias = Asistencia.objects.filter(
                    inscripcion=inscripcion
                ).order_by('fecha')

                presentes = asistencias.filter(
                    estado='P'
                ).count()

                ausentes = asistencias.filter(
                    estado='A'
                ).count()

                tardes = asistencias.filter(
                    estado='T'
                ).count()

                justificadas = asistencias.filter(
                    estado='J'
                ).count()

                total = asistencias.count()

                if total > 0:

                    porcentaje = round(
                        (presentes + tardes) / total * 100,
                        1
                    )

                else:

                    porcentaje = 0

                alumnos_reporte.append({

                    'inscripcion': inscripcion,

                    'asistencias': asistencias,

                    'presentes': presentes,

                    'ausentes': ausentes,

                    'tardes': tardes,

                    'justificadas': justificadas,

                    'total': total,

                    'porcentaje': porcentaje,

                })

    # ==================================================
    # MOSTRAR REPORTE
    # ==================================================

    return render(
        request,
        'asistencia/reportes/asistencia.html',
        {
            'ciclos': ciclos,

            'carreras': carreras,

            'anios': anios,

            'materias': materias,

            'alumnos_reporte': alumnos_reporte,

            'materia_seleccionada':
                materia_seleccionada,

            'ciclo_id': ciclo_id,

            'carrera_id': carrera_id,

            'anio_id': anio_id,

            'materia_id': materia_id,
        }
    )
# ==================================================
# BUSCADOR DE ALUMNOS
# ==================================================

def buscar_alumno_asistencia(request):

    buscar = request.GET.get('buscar', '').strip()

    alumnos = Alumno.objects.all().order_by(
        'apellido',
        'nombre'
    )

    # Si escribió algo, filtrar
    if buscar:

        alumnos = alumnos.filter(
            Q(nombre__icontains=buscar) |
            Q(apellido__icontains=buscar) |
            Q(dni__icontains=buscar)
        )

    alumno_seleccionado = None
    datos_materias = []

    alumno_id = request.GET.get('alumno')

    if alumno_id:

        alumno_seleccionado = get_object_or_404(
            Alumno,
            id=alumno_id
        )

        inscripciones = Inscripcion.objects.filter(
            alumno=alumno_seleccionado
        ).select_related(
            'materia',
            'materia__anio',
            'materia__anio__carrera',
            'ciclo_lectivo'
        ).order_by(
            'materia__anio__nombre',
            'materia__nombre'
        )

        for inscripcion in inscripciones:

            asistencias = Asistencia.objects.filter(
                inscripcion=inscripcion
            ).order_by('fecha')

            presentes = asistencias.filter(
                estado='P'
            ).count()

            ausentes = asistencias.filter(
                estado='A'
            ).count()

            tardes = asistencias.filter(
                estado='T'
            ).count()

            justificadas = asistencias.filter(
                estado='J'
            ).count()

            total = asistencias.count()

            if total > 0:
                porcentaje = round(
                    (presentes + tardes) / total * 100,
                    1
                )
            else:
                porcentaje = 0

            datos_materias.append({
                'materia': inscripcion.materia,
                'anio': inscripcion.materia.anio,
                'carrera': inscripcion.materia.anio.carrera,
                'ciclo': inscripcion.ciclo_lectivo,
                'asistencias': asistencias,
                'presentes': presentes,
                'ausentes': ausentes,
                'tardes': tardes,
                'justificadas': justificadas,
                'total': total,
                'porcentaje': porcentaje,
            })

    return render(
        request,
        'asistencia/buscador/buscador.html',
        {
            'buscar': buscar,
            'alumnos': alumnos,
            'alumno_seleccionado': alumno_seleccionado,
            'datos_materias': datos_materias,
        }
    )