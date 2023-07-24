// JavaScript code to handle unlocking character parts after watching an ad

// Function to unlock a character part
function unlockPart(partId) {
  const partImage = document.getElementById(partId + "-image");
  partImage.src = "unlocked-" + partId + ".png";
}

// Function to handle the ad watch button click
function watchAd() {
  // Disable the button to prevent multiple clicks during the ad watch
  const watchAdBtn = document.getElementById("watch-ad-btn");
  watchAdBtn.disabled = true;

  // Set the ad duration (30 seconds in this case)
  let adDuration = 30;

  // Display the countdown timer
  const timer = document.querySelector(".timer");
  timer.style.display = "block";

  // Update the countdown timer every second
  const countdownInterval = setInterval(() => {
    adDuration--;
    timer.textContent = adDuration;

    // If the ad is finished, unlock all character parts and reset the UI
    if (adDuration <= 0) {
      unlockPart("head"); // Unlock other parts here if needed
      timer.style.display = "none";
      watchAdBtn.disabled = false;
      clearInterval(countdownInterval);
    }
  }, 1000);
}

// Event listener for the watch ad button
document.getElementById("watch-ad-btn").addEventListener("click", watchAd);
