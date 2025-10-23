if (document.querySelector('.contenedorProducto')) {

    const btnAgregarAlCarrito = document.querySelectorAll('.btnAgregarAlCarrito');
    btnAgregarAlCarrito.forEach((boton) => {
        const inputCantidad = document.getElementById('inputCantidad');
        boton.addEventListener('click', () => {

            if (Number(document.querySelector('.span-stock').textContent) > 0) {
                const idProducto = boton.getAttribute('data-id');
                const nombreProducto = boton.getAttribute('data-nombre');
                const cantidad = inputCantidad.value;
                let carrito = [];

                if (localStorage.getItem('carrito')) {
                    carrito = JSON.parse(localStorage.getItem('carrito'));
                }

                const productoExistente = carrito.find(p => p.id === idProducto);

                if (productoExistente) {
                    productoExistente.cantidad = parseInt(productoExistente.cantidad) + parseInt(cantidad);
                } else {
                    const productoNuevo = {
                        'id': idProducto,
                        'nombre': nombreProducto,
                        'cantidad': cantidad
                    }
                    carrito.push(productoNuevo);
                }
                localStorage.setItem('carrito', JSON.stringify(carrito));

            } else {
                Swal.fire({
                    title: 'No hay stock disponible',
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 2500,
                })
            }
        })
    }
    )
}

if (document.getElementById('navbarSupportedContent') && document.getElementById('btnVaciarCarrito')) {
    const btnVaciarCarrito = document.getElementById('btnVaciarCarrito');
    btnVaciarCarrito.addEventListener('click', () => {
        if (!localStorage.getItem('carrito')) {
            Swal.fire({
                title: 'Su carrito ya se encuentra vacío.',
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 2500,
            })
        } else {
            localStorage.clear();
            Swal.fire({
                title: 'Se ha vaciado su carrito.',
                icon: 'success',
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 3000,
            })
        }
    })
}
