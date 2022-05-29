from django.contrib import admin
from .models import *
# Register your models here.


class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','descripcion','stock','tipo','imagen','created_at','updated_at']
    search_fields = ['codigo']
    list_per_page = 3

class UserAdmin(admin.ModelAdmin):
    list_display = ['run','nombre','apellido','email','contraseña','sub','direccion']
    search_fields = ['run']
    list_per_page = 3

class CarritoAdmin(admin.ModelAdmin):
     list_display = ['producto']
     search_fields = ['codigo']
     list_per_page = 3




admin.site.register(TipoProducto)
admin.site.register(Producto,ProductosAdmin)
admin.site.register(Usuario,UserAdmin)
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(TipoPago)
admin.site.register(Estado)
