document.addEventListener("DOMContentLoaded", () => {
    const textToType = "👋, my name is Gourav Kumar and I am a B.Tech Student";
    const typeWriterElement = document.getElementById("typewriter-text");
    
    let charIndex = 0;
    
    function typeWriter() {
        if (charIndex < textToType.length) {
            typeWriterElement.textContent += textToType.charAt(charIndex);
            charIndex++;
            setTimeout(typeWriter, 50); // Adjust typing speed here (ms)
        }
    }
    
    // Start typing after a short delay
    setTimeout(typeWriter, 500);
});
