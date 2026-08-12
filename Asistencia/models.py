from django.db import models


# ==================================================
# CICLO LECTIVO
# ==================================================

class CicloLectivo(models.Model):

    nombre = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return self.nombre


# ==================================================
# CARRERA
# Cada carrera pertenece a un ciclo lectivo.
# ==================================================

class Carrera(models.Model):

    ciclo_lectivo = models.ForeignKey(
        CicloLectivo,
        on_delete=models.CASCADE,
        related_name='carreras'
    )

    nombre = models.CharField(
        max_length=150
    )

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    'ciclo_lectivo',
                    'nombre'
                ],
                name='carrera_unica_por_ciclo'
            )

        ]

        ordering = [
            'ciclo_lectivo__nombre',
            'nombre'
        ]

    def __str__(self):
        return f"{self.nombre} - {self.ciclo_lectivo}"
    @property
    def nombre_corto(self):

        nombre = self.nombre

        nombre = nombre.replace(
            'Profesorado de ',
            'Prof. '
        )

        nombre = nombre.replace(
            'Tecnicatura Superior en ',
            'Tec. '
        )

        return nombre

    def __str__(self):
        return self.nombre


# ==================================================
# AÑO
# Cada año pertenece a una carrera.
# ==================================================

class Anio(models.Model):

    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE,
        related_name='anios'
    )

    nombre = models.CharField(
        max_length=50
    )

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    'carrera',
                    'nombre'
                ],
                name='anio_unico_por_carrera'
            )

        ]

        ordering = [
            'carrera__nombre',
            'nombre'
        ]

    def __str__(self):
        return f"{self.nombre} - {self.carrera}"


# ==================================================
# MATERIA
# Cada materia pertenece a un año.
# La carrera se obtiene desde el año.
# ==================================================

class Materia(models.Model):

    anio = models.ForeignKey(
        Anio,
        on_delete=models.CASCADE,
        related_name='materias'
    )

    nombre = models.CharField(
        max_length=150
    )

    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    'anio',
                    'nombre'
                ],
                name='materia_unica_por_anio'
            )

        ]

        ordering = [
            'anio__carrera__nombre',
            'anio__nombre',
            'nombre'
        ]

    def __str__(self):
        return f"{self.nombre} - {self.anio}"

# ==================================================
# ALUMNO
# ==================================================

class Alumno(models.Model):

    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.PROTECT,
        related_name='alumnos'
    )


    apellido = models.CharField(
        max_length=150
    )

    nombre = models.CharField(
        max_length=150
    )

    dni = models.CharField(
        max_length=8,
        unique=True
    )

    class Meta:

        ordering = [
            'apellido',
            'nombre'
        ]

    def __str__(self):

        return (
            f"{self.apellido}, "
            f"{self.nombre}"
        )
# ==================================================
# INSCRIPCION
# Alumno cursa una materia en un ciclo lectivo
# ==================================================

class Inscripcion(models.Model):

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )

    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )

    ciclo_lectivo = models.ForeignKey(
        CicloLectivo,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=[
                    'alumno',
                    'materia',
                    'ciclo_lectivo'
                ],
                name='inscripcion_unica'
            )
        ]

    def __str__(self):

        return f"{self.alumno} - {self.materia}"
# ==================================================
# ASISTENCIA
# Una asistencia corresponde a una inscripción y una fecha
# ==================================================

class Asistencia(models.Model):

    ESTADOS = (

        ('P', 'Presente'),
        ('A', 'Ausente'),
        ('T', 'Tarde'),
        ('J', 'Justificada'),

    )

    inscripcion = models.ForeignKey(
        Inscripcion,
        on_delete=models.CASCADE,
        related_name='asistencias'
    )

    fecha = models.DateField()

    estado = models.CharField(
        max_length=1,
        choices=ESTADOS,
        default='P'
    )


    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=[
                    'inscripcion',
                    'fecha'
                ],
                name='asistencia_unica'
            )
        ]


    def __str__(self):

        return (
            f"{self.fecha} - "
            f"{self.inscripcion}"
        )
