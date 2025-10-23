if (document.getElementById('cantidadItemsCarrito')){
    const url = '/api/subtotales/';
    fetch(url)
        .then(res => res.json())
        .then(res => logearProductos(res))
        .catch(err => console.error("Error cargando JSON:", err))

    function logearProductos(subtotales) {
        if (subtotales[0]==null) {
            console.log('No hay nada en el carrito')
            document.getElementById('cantidadItemsCarrito').textContent=0
            document.getElementById('totalMiniCarrito').textContent=0
        } else{
            const arrayCantidad = [];
            subtotales.forEach((producto) => {
                arrayCantidad.push(producto)
            })
            for (const element of arrayCantidad) {
                console.log(element.cantidad_total_productos, 'Total productos agregados en el carrito ', element.id)
            }
    
            console.log(arrayCantidad[0].cantidad_total_productos, 'Total productos mostrando la posicion 0 del array')
    
            document.getElementById('cantidadItemsCarrito').textContent=arrayCantidad[0].cantidad_total_productos;
            document.getElementById('totalMiniCarrito').textContent=arrayCantidad[0].subtotal
        }
}}