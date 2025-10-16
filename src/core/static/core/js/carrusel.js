if (document.querySelector('.ulCarrusel')) {
  document.addEventListener('DOMContentLoaded', async () => {
    const ulCarrusel = document.querySelector('.ulCarrusel');

    new Swiper('.card-wrapper', {
      slidesPerView: 3,
      spaceBetween: 30,
      loop: true,
      spaceBetween: 30,

      // Paginations bullets
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },

      // Navigation arrows
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      //Responsive breakpoints
      breakpoints: {
        0: {
          slidesPerView: 1,
          spaceBetween: 10
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 20
        },
        1024: {
          slidesPerView: 3,
          spaceBetween: 30
        },
        1440: {
          slidesPerView: 4,
          spaceBetween: 40
        }
      }
    });

    try {
      const res = await fetch('/api/productos/');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);

      const productos = await res.json();

      productos.forEach(prod => {
        const li = document.createElement('li');
        li.className = 'card-item swiper-slide';
        li.innerHTML = `
                <a href="#" class="card-link">
                    <img src="${prod.imagen_url}" alt="Card Imagen ${prod.nombre}"
                        class="card-image">
                    <hr>
                    <p class="badge">${prod.nombre}</p>
                    <button class="card-button">
                        VER PRODUCTO
                    </button>
                </a>
                `;
        ulCarrusel.appendChild(li);
      });
    } catch (err) {
      console.error('Error cargando productos:', err);
    }
  });
}



const IMG_PATH = "/static/core/assets/img/"; //Ruta de las imagenes
const IMG_CARRITO_MARRON = `${IMG_PATH}carritoComprasMarron.png`;
const IMG_CARRITO_BLANCO = `${IMG_PATH}carritoComprasBlanco.png`;

if (document.querySelector('.anclaComprarYara')) {
  const anclaCompraYara = document.querySelector('.anclaComprarYara');

  anclaCompraYara.addEventListener('mouseover', () => {
    document.querySelector('.anclaComprarYara').innerHTML = `
    COMPRÁ YARÁ
    <img id="imgCarritoYara" src="${IMG_CARRITO_MARRON}" alt="" style="width: 24px;">
  `
  });

  anclaCompraYara.addEventListener('mouseout', () => {
    document.querySelector('.anclaComprarYara').innerHTML = `
      COMPRÁ YARÁ
      <img id="imgCarritoYara" src="${IMG_CARRITO_BLANCO}" alt="" style="width: 24px;">
    `
  })
}

