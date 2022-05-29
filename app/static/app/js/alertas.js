function prueba(){
  Swal.fire({
    position: 'top-end',
    icon: 'success',
    title: 'Your work has been saved',
    showConfirmButton: false,
    timer: 1500
  })
}
function xd(){
    Swal.fire({
        icon: 'error',
        title: 'Ups! ',
        text: 'Debes logearte para poder comprar',
      
      })
}


function confirmDelete(codigo) {
    Swal.fire({
        icon: 'warning',
        title: 'Estás seguro?',
        text: 'No podrás deshacer la acción!',
        showCancelButton: true,
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, Eliminar!",
        confirmButtonColor: '#3085d6',
        cancelButtonText: "Cancelar"
      }).then((result) => {
        if (result.value) {
          Swal.fire(
            'Eliminado!',
            'Producto Eliminado Correctamente',
            'success'
          ).then(function() {
            window.location.href = "/eliminar_carrito/"+ codigo +"/";
          })
        }
      })
  }

  function confirmDeleteUser(run) {
    Swal.fire({
        icon: 'warning',
        title: 'Estás seguro?',
        text: 'No podrás deshacer la acción!',
        showCancelButton: true,
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, Eliminar!",
        confirmButtonColor: '#3085d6',
        cancelButtonText: "Cancelar"
      }).then((result) => {
        if (result.value) {
          Swal.fire(
            'Eliminado!',
            'Producto Eliminado Correctamente',
            'success'
          ).then(function() {
            window.location.href = "/eliminar_user/"+ run +"/";
          })
        }
      })
  }