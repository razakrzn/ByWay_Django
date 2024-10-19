document
  .querySelectorAll(".custom-swiper-button-next, .custom-swiper-button-prev")
  .forEach((button) => {
    button.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        console.log("Button clicked via keyboard");
        button.click();
      }
    });
  });

const swiper = new Swiper(".swiper", {
  loop: true,
  slidesPerView: 3,
  spaceBetween: 15,
  slidesPerGroup: 3,

  pagination: {
    el: ".swiper-pagination",
  },

  navigation: {
    nextEl: ".custom-swiper-button-next",
    prevEl: ".custom-swiper-button-prev",
  },

  scrollbar: {
    el: ".swiper-scrollbar",
  },

  keyboard: {
    enabled: true, // Enable keyboard control
    onlyInViewport: true,
  },

  breakpoints: {
    320: {
      slidesPerView: 1,
      slidesPerGroup: 1,
    },
    360: {
      slidesPerView: 1,
      slidesPerGroup: 1,
    },
    480: {
      slidesPerView: 1,
      slidesPerGroup: 1,
    },
    600: {
      slidesPerView: 1,
      slidesPerGroup: 1,
      spaceBetween: 20,
    },
    768: {
      slidesPerView: 2,
      slidesPerGroup: 2,
    },
    1024: {
      slidesPerView: 3,
      slidesPerGroup: 3,
    },
  },
});
