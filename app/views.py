from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    productoTodos = Producto.objects.all()
    datos = {
        'form' : UserForm(),
        'listaProductos': productoTodos
    }
    if request.method == 'POST':
        formulario = UserForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario guardado correctamente!'

    return render(request,'app/index.html',datos)

# ------------------PRODUCTO----------------------------
# AGREGAR
def agregar_producto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
        else:
            formulario.errors    
    return render(request, 'app/producto/agregar_producto.html',datos)
#LISTAR
def listar_productos(request):
    productoTodos = Producto.objects.all()
    datos ={
        'listaProductos': productoTodos
    }
    return render(request, 'app/producto/listar_producto.html',datos)
# MODIFICAR
def modificar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto Editado correctamente!')
            datos['mensaje'] = 'Producto modificado correctamente!'
            datos['form'] = formulario
            
    return render(request, 'app/producto/modificar_producto.html',datos)    
# SECCION ELIMINAR
def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar_producto")
#------------------------------------------------------------------------------------------

#------------------USER---------------------------------
def user(request):
    productoTodos = Producto.objects.all()
    datos ={
        'listaProductos': productoTodos
    }

    if request.method == 'POST':

        tipo = TipoProducto()
        tipo.tipo = request.POST.get('tipo')

        producto = Producto()
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.marca = request.POST.get('marca')
        producto.precio = request.POST.get('precio')
        producto.descripcion = request.POST.get('descripcion')
        producto.stock = request.POST.get('stock')
        producto.tipo = tipo
        producto.imagen = request.POST.get('imagen')
        producto.created_at = request.POST.get('created_at')
        producto.updated_at = request.POST.get('updated_at')


        carrito = Carrito()
        carrito.producto = producto
        
        carrito.save()
        
    return render(request, 'app/user/user.html',datos)


# CREACION DE USER
#PAGINA INDEX
def index(request):
    productoTodos = Producto.objects.all()
    datos = {
        'form' : UserForm(),
        'listaProductos': productoTodos
    }
    if request.method == 'POST':
        formulario = UserForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario guardado correctamente!'

    return render(request,'app/index.html',datos)

#LISTAR
def listar_user(request):
    userTodos = User.objects.all()
    datos ={
        'listaUser': userTodos
    }
    return render(request, 'app/user/listar_user.html',datos)
#MODIFICAR
def modificar_user(request, run):
    user = User.objects.get(run=run)
    datos = {
        'form' : UserForm(instance=user)
    }
    if request.method == 'POST':
        formulario = UserForm(request.POST, files=request.FILES,instance=user)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario modificado correctamente!'
            datos['form'] = formulario
            
    return render(request, 'app/user/modificar_user.html',datos)       
#ELIMINAR
def eliminar_user(request, run):
    user = User.objects.get(run=run)
    user.delete()

    return redirect(to="listar_user")



#---------------CARRO--------------------
# VISTA CARRO
def carrito(request):
    carroTodos = Carrito.objects.all()
    datos ={
        'listaCarro': carroTodos
    }
    datos['total'] = 0


    return render(request, 'app/carrito/carrito.html',datos)   
#BORRAR
def eliminar_carrito(request, codigo):
    carrito = Carrito.objects.get(codigo=codigo)
    carrito.delete()   


    return redirect(to="carrito")


# VISTA LOGIN





def perfil(request):
    return render(request, 'app/perfil/perfil.html')

def seguimiento(request):
    return render(request, 'app/perfil//seguimiento.html')

def compras(request):
    return render(request, 'app/perfil/compras.html')

def register(request):
    datos = {
        'form' : UserCreationForm()  
    }
    if request.method == 'POST':
        formulario = UserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            messages.success(request,'Registrado correctamente!')
            #return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/register.html', datos)






