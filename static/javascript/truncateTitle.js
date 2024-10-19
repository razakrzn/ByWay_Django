function truncateElements() {
  const titleElements = document.querySelectorAll(".course-title");
  titleElements.forEach((titleElement) => {
    let titleText = titleElement.getAttribute("data-full-title");

    titleElement.textContent = titleText;

    if (window.innerWidth >= 1440) {
        if (titleText.length > 24) {
          titleElement.textContent = titleText.substring(0, 24) + "...";
        }
      } else if (window.innerWidth >= 1280 && window.innerWidth < 1440) {
        if (titleText.length > 30) {
          titleElement.textContent = titleText.substring(0, 30) + "...";
        }
      } else if (window.innerWidth >= 768 && window.innerWidth < 980) {
        if (titleText.length > 30) {
          titleElement.textContent = titleText.substring(0, 30) + "...";
        }
      }
  });

  const durationElements = document.querySelectorAll(".duration");
  durationElements.forEach((durationElement) => {
    let durationText = durationElement.getAttribute("data-full-duration");

    durationElement.textContent = durationText;

    if (window.innerWidth > 1280) {
      if (durationText.length > 37) {
        durationElement.textContent = durationText.substring(0, 37) + "...";
      }
    }
  });
}

// Attach event listeners for resize and load events
window.addEventListener("resize", truncateElements);
window.addEventListener("load", truncateElements);
