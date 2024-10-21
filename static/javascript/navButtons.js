function smoothScroll(target, duration) {
    let targetPosition = document.querySelector(target).getBoundingClientRect().top;
    let startPosition = window.pageYOffset;
    let distance = targetPosition;
    let startTime = null;
  
    function animation(currentTime) {
      if (startTime === null) startTime = currentTime;
      let timeElapsed = currentTime - startTime;
      let run = ease(timeElapsed, startPosition, distance, duration);
      window.scrollTo(0, run);
      if (timeElapsed < duration) requestAnimationFrame(animation);
    }
  
    function ease(t, b, c, d) {
      t /= d / 2;
      if (t < 1) return c / 2 * t * t + b;
      t--;
      return -c / 2 * (t * (t - 2) - 1) + b;
    }
  
    requestAnimationFrame(animation);
  }
  
  document.querySelectorAll('.button-container button').forEach(button => {
    button.addEventListener('click', function() {
      const targetSection = this.getAttribute('data-target');
      smoothScroll(targetSection, 300); 
    });
  });
  