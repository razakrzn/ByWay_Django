document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('see-all-button').addEventListener('click', function (event) {
        event.preventDefault(); 
        const remainingInstructors = document.getElementById('remaining-instructors');
        remainingInstructors.style.display = 'block'; 
        this.style.display = 'none'; 
    });
});
