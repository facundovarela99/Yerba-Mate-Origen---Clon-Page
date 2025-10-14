if (document.querySelector('.tarjetasProductos')){
    document.addEventListener('DOMContentLoaded', async () => {
    const contenedor = document.querySelector('.tarjetasProductos');

    try {
        const res = await fetch('/productos/api/productos/');
        if (!res.ok) throw new Error(`HTTP ${res.status}`);

        const productos = await res.json();

        function stock(value){
            if (value<=0){
                return 'SIN STOCK';
            } return '';
        }

        productos.forEach(prod => {
            const div = document.createElement('div');
            div.className = `producto${prod.id}`
            div.innerHTML = `
                <img class="imgProducto" src="${prod.imagen_url}" alt="${prod.nombre}"/>
                <h2 class="nombreProducto">${prod.nombre}</h2>
                <p class="precioProducto"><strong>$${prod.precio}</strong></p>
                <button id="botonProducto${prod.id}" type="button">VER PRODUCTO</button>
                <p>${stock(prod.stock)}</p>
            `;
            contenedor.appendChild(div);
        });
    } catch (err) {
        console.error('Error cargando productos:', err);
    }
});

}