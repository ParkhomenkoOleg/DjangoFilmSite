const slides = document.querySelectorAll('.heroes>li');
const dots = document.querySelectorAll(".spans>span");
const interval = 5;

let activeSlide = 0;


const reset = () => {
    dots.forEach(dot => dot.removeAttribute('class'));
    dots[activeSlide].className = 'active';
    slides.forEach(slide => slide.style.display = 'none');
    slides[activeSlide].style.display = 'block';
}

reset();

setInterval(() => {
  reset();
  if(activeSlide < slides.length - 1) {
    activeSlide++;
  } else {

  activeSlide = 0;
  }



}, interval * 1000);

dots.forEach((dot, index) => {
  dot.addEventListener('click', () => {
  activeSlide = index;
  reset();

  });
});

const checkpoint = 500;
let nav_bg='transparent';
let opacity = 1;
window.addEventListener("scroll", ()=> {
  const currentScroll = window.pageYOffset;
  if (currentScroll <= checkpoint) {
    nav_bg = 'transparent';
    opacity = 1 - currentScroll / checkpoint;
  } else {
    nav_bg = '#0C0B0B';
    opacity = 0;
  }

  document.querySelector(".header-nav").style.background = nav_bg;
  slides.forEach(slide => slide.getElementsByTagName('img')[0].style.opacity = opacity);
});