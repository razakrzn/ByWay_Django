
const fullStarPath = "/static/assets/icons/star.svg";
const emptyStarPath = "/static/assets/icons/EmptyStar.svg";

const starPattern = [
    { stars: [true, true, true, true, true], percentage: "80%" },
    { stars: [true, true, true, true, false], percentage: "10%" },
    { stars: [true, true, true, false, false], percentage: "5%" },
    { stars: [true, true, false, false, false], percentage: "3%" },
    { stars: [true, false, false, false, false], percentage: "2%" },
];

function renderStarPyramid() {
    const container = document.getElementById('star-pyramid-container');
    
    starPattern.forEach(row => {
        const rowDiv = document.createElement('div');
        rowDiv.style.display = 'flex';
        rowDiv.style.alignItems = 'center';
        rowDiv.style.margin = '5px 0';

        const starsDiv = document.createElement('div');
        starsDiv.style.display = 'flex';

        row.stars.forEach(isFull => {
            const starImg = document.createElement('img');
            starImg.src = isFull ? fullStarPath : emptyStarPath;
            starImg.alt = isFull ? 'Full Star' : 'Empty Star';
            starImg.style.width = '18px';
            starImg.style.height = '18px';
            starImg.style.margin = '0 2px';
            starsDiv.appendChild(starImg);
        });

        const percentageSpan = document.createElement('span');
        percentageSpan.textContent = row.percentage;
        percentageSpan.style.marginLeft = '10px';
        percentageSpan.style.fontSize = '14px';
        percentageSpan.style.color = '#333';

        rowDiv.appendChild(starsDiv);
        rowDiv.appendChild(percentageSpan);

        container.appendChild(rowDiv);
    });
}

document.addEventListener('DOMContentLoaded', renderStarPyramid);
