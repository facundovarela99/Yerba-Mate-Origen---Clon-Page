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
    breakpoints:{
    0:{
        slidesPerView: 1,
        spaceBetween: 10
    },
    768:{
        slidesPerView: 2,
        spaceBetween: 20
    },
    1024:{
        slidesPerView: 3,
        spaceBetween: 30
    },
    1440:{
      slidesPerView: 4,
      spaceBetween: 40
    }
  }
});

const IMG_PATH = "/static/core/assets/img/";
const IMG_CARRITO_MARRON = `${IMG_PATH}carritoComprasMarron.png`;
const IMG_CARRITO_BLANCO = `${IMG_PATH}carritoComprasBlanco.png`;

const anclaCompraYara = document.querySelector('.anclaComprarYara');

anclaCompraYara.addEventListener('mouseover',()=>{
  document.querySelector('.anclaComprarYara').innerHTML=`
  COMPRÁ YARÁ
  <img id="imgCarritoYara" src="${IMG_CARRITO_MARRON}" alt="" style="width: 24px;">
`
});

anclaCompraYara.addEventListener('mouseout',()=>{
  document.querySelector('.anclaComprarYara').innerHTML = `
    COMPRÁ YARÁ
    <img id="imgCarritoYara" src="${IMG_CARRITO_BLANCO}" alt="" style="width: 24px;">
  `
})
