// Smooth scrolling for the Contact Us button
document.getElementById('contactBtn').addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector('#contact').scrollIntoView({ behavior: 'smooth' });
});

// Alert on hover over destinations - only once
document.querySelectorAll('.dest').forEach(dest => {
    let hovered = false; // Initialize a flag for each destination
    dest.addEventListener('mouseover', function () {
        if (!hovered) {
            alert(`Discover more about ${this.dataset.destination}!`);
            hovered = true; // Set flag to true after the first hover
        }
    });
});
