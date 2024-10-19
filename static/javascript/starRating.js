function createStarRating(rating) {
    const container = document.createElement("div");
    container.style.display = "flex";
    container.style.gap = "2px";

    const starSize = window.innerWidth <= 480 ? "14px" : "18px";
    const fullStars = Math.floor(rating);
    const halfStar = rating % 1 >= 0.5;
    const emptyStars = 5 - fullStars - (halfStar ? 1 : 0);

    const FullStar = "/static/assets/icons/star.svg"; 
    const HalfStar = "/static/assets/icons/halfstar.svg"; 
    const EmptyStar = "/static/assets/icons/unfilstar.svg"; 

    for (let i = 0; i < fullStars; i++) {
        const img = document.createElement("img");
        img.src = FullStar;
        img.alt = "Full Star";
        img.style.width = starSize;
        img.style.height = starSize;
        container.appendChild(img);
    }

    if (halfStar) {
        const img = document.createElement("img");
        img.src = HalfStar;
        img.alt = "Half Star";
        img.style.width = starSize;
        img.style.height = starSize;
        container.appendChild(img);
    }

    // Create empty stars
    for (let i = 0; i < emptyStars; i++) {
        const img = document.createElement("img");
        img.src = EmptyStar;
        img.alt = "Empty Star";
        img.style.width = starSize;
        img.style.height = starSize;
        container.appendChild(img);
    }

    return container;
}

document.addEventListener("DOMContentLoaded", function () {
    const ratings = document.querySelectorAll(".rating");  
    ratings.forEach(function (ratingElement) {
        const rating = parseFloat(ratingElement.innerText);  
        const starContainer = createStarRating(rating);      
        const starContainerElement = ratingElement.nextElementSibling; 
        if (starContainerElement && starContainerElement.classList.contains('star-rating-container')) {
            starContainerElement.appendChild(starContainer);  
        }
    });
});
