from django import forms
from api.models import Mascota , Usuario


#PERFILES DE USUARIO
perfiles=(
    ('Adoptante','Adoptante'),
)


#LUGAR DE VIVIENDA DEL USUARIO
ubicacion= (
    ('Metropolitana', (
            ('Chacabuco', 'Chacabuco'),
            ('Cordillera', 'Cordillera'),
            ('Maipo','Maipo'),
            ('Melipilla','Melipilla'),
            ('Santiago','Santiago'),
            ('Talagante', 'Talagante'),
        )
    ),
    ('Valparaiso', (
            ('Valparaiso', 'Valparaiso'),
            ('Viña del mar', 'Viña del mar'),
        )
    ),
)

tipovivienda=(
    ('casa con patio grande','casa con patio grande'),
    ('casa con patio pequeño','casa con patio pequeño'),
    ('casa sin patio','casa sin patio'),
    ('departamento','departamento'),

)

#ESTADO DE LA MASCOTA
estados=(
    ('Rescatado', 'Rescatado'),
    ('Adoptado', 'Adoptado'),
    ('Disponible', 'Disponible'),
)

#AGREGAR USUARIOS
class AgregarUsuario(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")
    contacto=forms.CharField(widget=forms.TextInput(),label="telefono")
    region=forms.ChoiceField(choices=ubicacion,label="Ubicacion")
    vivienda=forms.ChoiceField(choices=tipovivienda,label="tipo vivienda")#CHOICE FIELD PARA DESPLEGAR UNA LISTA(TUPLA)
    perfil=forms.ChoiceField(choices=perfiles)


#INGRESAR AL SISTEMA
class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")

#CLASE DE LA MASCOTA
class Mascotas(forms.Form):
    fotoMascota=forms.ImageField()
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre Mascota")
    razaMascota=forms.CharField(widget=forms.TextInput(),label="Raza Mascota")
    descripcionMascota=forms.CharField(widget=forms.TextInput(),label="Descripcion")
    estado=forms.ChoiceField(choices=estados, initial='Rescatado')
    

#INTENTOS FALLIDOS O CAMBIADOS

"""
class Mascotas(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = [
        'nombreMascota',
        'razaMascota',
        'descripcionMascota',
        'estado'
    ]

    labels = {
        'nombreMascota':'Nombre Mascota',
        'razaMascota':'Raza Mascota',
        'descripcionMascota':'Descripcion',
        'estado' : 'Estado'
    }
    estado=forms.ChoiceField(choices=estados, initial='Rescatado')
    widgets ={
        'nombreMascota': forms.TextInput(attrs={'class':'form=control'}),
        'razaMascota': forms.TextInput(attrs={'class':'form=control'}),
        'descripcionMascota': forms.TextInput(attrs={'class':'form=control'}),
        
    }

"""

"""
class Formulario(forms.Form):
    rut=forms.CharField(widget=forms.NumberInput(),label="Rut")
    nombre=forms.CharField(widget=forms.TextInput(),label="Nombre Completo")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")
"""
      
"""
class AgregarMascota(forms.Form):
    rutmascota=forms.CharField(widget=forms.NumberInput(),label="Rut Mascota")
    nombremascota=forms.CharField(widget=forms.TextInput(),label="Nombre")
    raza=forms.CharField(widget=forms.TextInput(),label="Raza")
    descripcion=forms.CharField(widget=forms.TextInput(),label="Descripcion")
    perfil=forms.ChoiceField(choices=perfilesM)      
"""    