from django import forms
from .models import Carrera, CicloLectivo, Anio, Materia, CicloLectivo,Alumno


# =========================
# FORMULARIO DE CICLO LECTIVO
# =========================

class CicloLectivoForm(forms.ModelForm):

    class Meta:
        model = CicloLectivo
        fields = ['nombre']

        labels = {
            'nombre': 'Ciclo lectivo'
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: 2026',
                    'maxlength': '10'
                }
            )
        }

# =========================
# FORMULARIO DE CARRERAS
# =========================

class CarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera
        fields = ['nombre','ciclo_lectivo']

        labels = {
            'nombre': 'Nombre de la Carrera'
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Tecnicatura Superior en Desarrollo de Software'
                }
            )
        }

# =========================
# FORMULARIO DE AÑOS
# =========================

class AnioForm(forms.ModelForm):

    class Meta:
        model = Anio
        fields = ['nombre']

        labels = {
            'nombre': 'Nombre del año'
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: 1° Año'
                }
            )
        }

# =========================
# FORMULARIO DE MATERIAS
# =========================

class MateriaForm(forms.ModelForm):

    class Meta:

        model = Materia

        fields = ['nombre']

        labels = {
            'nombre': 'Nombre de la materia'
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Introducción al Turismo'
                }
            )
        }


# ==================================================
# FORMULARIO DE ALUMNO
# ==================================================

class AlumnoForm(forms.ModelForm):

    class Meta:

        model = Alumno

        fields = [
            'apellido',
            'nombre',
            'dni',
            'carrera',
        ]

        labels = {
            'apellido': 'Apellido',
            'nombre': 'Nombre',
            'dni': 'DNI',
            'carrera': 'Carrera',
        }

        widgets = {

            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido'
                }
            ),

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),

            'dni': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'DNI',
                    'maxlength': '8'
                }
            ),

            'carrera': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

