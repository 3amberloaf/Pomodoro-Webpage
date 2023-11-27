let timer;
let timerDuration = 25 * 60; // Default timer duration is 25 minutes

function updateTimerDisplay() {
  const minutes = Math.floor(timerDuration / 60);
  const seconds = timerDuration % 60;
  document.getElementById('countdown').textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function startTimer() {
  timer = setInterval(function() {
    if (timerDuration > 0) {
      timerDuration--;
      updateTimerDisplay();
    } else {
      clearInterval(timer);
      document.getElementById('countdown').textContent = "Break Time!";
    }
  }, 1000);
}

function stopTimer() {
  clearInterval(timer);
}

document.getElementById('duration').addEventListener('change', function() {
  timerDuration = this.value * 60;
  updateTimerDisplay();
});
