from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  


# TEMPLATE FORMULARIO

class ProductoForm(ModelForm):

  # formulario validaciones

    nombre = forms.CharField(min_length=10,max_length=20)
    precio = forms.IntegerField(min_value=400)

    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','descripcion','stock','tipo','imagen']

        widgets = {
            'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
        }

class UserForm(ModelForm):

  # formulario validaciones

    run = forms.IntegerField(min_value=10000000)
    contraseña = forms.CharField(widget=forms.PasswordInput,min_length=8)
    

    class Meta:
        model = Usuario
        fields = ['run','nombre','apellido','email','contraseña','direccion','imagen']

        widgets = {
            'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
        }

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']



