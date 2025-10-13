if (document.querySelector('.tarjetasProductos')){
    document.addEventListener('DOMContentLoaded', async () => {
    const contenedor = document.querySelector('.tarjetasProductos');

    try {
        const res = await fetch('/productos/api/productos/'); // 👈 URL completa
        if (!res.ok) throw new Error(`HTTP ${res.status}`);

        const productos = await res.json();

        productos.forEach(prod => {
            const div = document.createElement('div');
            div.classList.add('producto');
            div.innerHTML = `
                <h2>${prod.nombre}</h2>
                <p>${prod.descripcion}</p>
                <p><strong>$${prod.precio}</strong></p>
            `;
            contenedor.appendChild(div);
        });
    } catch (err) {
        console.error('Error cargando productos:', err);
    }
});

}