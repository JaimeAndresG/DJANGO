
from django.db import models

# Create your models here.
class TipoProducto (models.Model):
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo
        
    class Meta:
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=20)
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'db_producto'

class Usuario(models.Model):
    run = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=40)
    sub = models.BooleanField(default=False)
    direccion = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to="usuarios", null=True)

    def __str__(self):
        return self.run

        
    class Meta:
        db_table = 'db_user'

class Carrito(models.Model):
    codigo = models.AutoField(null=False,primary_key=True)

    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)

    def __str__(self):
        return self.codigo
        
    class Meta:
        db_table = 'db_carrito'

class TipoPago(models.Model):
     tipopago = models.CharField(max_length=30)

     def __str__(self):
        return self.tipopago
        
     class Meta:
        db_table = 'db_tipo_pago'

class Estado(models.Model):
    estado = models.CharField(max_length=30)

    def __str__(self):
        return self.estado
        
    class Meta:
        db_table = 'db_estado'    



    



    
