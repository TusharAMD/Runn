document.addEventListener('DOMContentLoaded', () => {
    const basket = document.querySelector('.basket');
    const log = document.querySelector('.log');
    const fireLevelDisplay = document.getElementById('fire-level');

    let fireLevel = 100;

    document.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowLeft') {
            moveBasket(-20);
        } else if (event.key === 'ArrowRight') {
            moveBasket(20);
        }
    });

    function moveBasket(offset) {
        const currentLeft = parseInt(getComputedStyle(basket).left);
        const newLeft = Math.max(0, Math.min(window.innerWidth - 80, currentLeft + offset));
        basket.style.left = `${newLeft}px`;
    }

    function dropLog() {
        const initialPosition = Math.random() * (window.innerWidth - 50);
        log.style.left = `${initialPosition}px`;
        log.style.top = '0';

        const fallInterval = setInterval(() => {
            const currentTop = parseInt(getComputedStyle(log).top);
            const newTop = currentTop + 3;

            if (newTop >= window.innerHeight - 60) {
                clearInterval(fallInterval);

                // Check if the log is caught
                checkCatch();

                // Respawn the log
                setTimeout(() => {
                    log.style.display = 'block';
                    dropLog();
                }, 1000);
            } else {
                log.style.top = `${newTop}px`;
            }
        }, 20);
    }

    function checkCatch() {
        const basketRect = basket.getBoundingClientRect();
        const logRect = log.getBoundingClientRect();

        if (
            logRect.left < basketRect.right &&
            logRect.right > basketRect.left &&
            logRect.bottom > basketRect.top &&
            logRect.top < basketRect.bottom
        ) {
            // Log caught
            fireLevel += 10;
        } else {
            // Log missed
            fireLevel -= 20;
        }

        // Update fire level display
        fireLevelDisplay.textContent = fireLevel;

        // If fire level drops to 0, game over
        if (fireLevel <= 0) {
            gameOver();
        }
    }

    function gameOver() {
        alert('Game Over! The fire went out.');
        location.reload(); // Reload the page to restart the game
    }

    // Start dropping logs
    dropLog();
});
