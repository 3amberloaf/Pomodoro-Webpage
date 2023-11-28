let countdownInterval;

function startTimer() {
    let duration = parseInt(document.getElementById('duration').value);
    if (isNaN(duration) || duration < 1) {
        alert("You can study more!");
        return;
    }

    let endTime = Date.now() + duration * 60000; // Convert minutes to milliseconds
    let lastSecond = -1;

    countdownInterval = setInterval(() => {
        let currentTime = Date.now();
        let timeLeft = endTime - currentTime;

        if (timeLeft <= 0) {
            clearInterval(countdownInterval);
            document.getElementById('countdown').textContent = "00:00";
            alert("Time's up!");
            return;
        }

        let currentSecond = Math.floor((timeLeft % 60000) / 1000);
        if (currentSecond !== lastSecond) {
            lastSecond = currentSecond;
            let minutes = Math.floor(timeLeft / 60000);
            let seconds = currentSecond;
            document.getElementById('countdown').textContent = `${pad(minutes)}:${pad(seconds)}`;
        }
    }, 100); // Check every 100 milliseconds
}

function pad(number) {
    return number < 10 ? '0' + number : number;
}

function stopTimer() {
    clearInterval(countdownInterval);
    document.getElementById('countdown').textContent = "00:00";
}
