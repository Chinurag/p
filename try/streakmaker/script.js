let streak = 0;
const streakInterval = 1; // minutes
const rewardThresholds = [7, 10]; // Streak thresholds for rewards

function completeTask() {
    streak++;
    document.getElementById("streakCount").textContent = `Streak: ${streak}`;
    
    checkRewards();
}

function checkRewards() {
    for (let i = 0; i < rewardThresholds.length; i++) {
        if (streak === rewardThresholds[i]) {
            showReward(i + 1);
            toggleTheme();
            break;
        }
    }
}

function showReward(rewardNumber) {
    const rewardDiv = document.getElementById("reward");
    rewardDiv.textContent = `Congratulations! You've earned reward number ${rewardNumber}!`;
    showPopup();
}

function showPopup() {
    const popup = document.getElementById("popup");
    popup.classList.remove("hidden");
}

function closePopup() {
    const popup = document.getElementById("popup");
    popup.classList.add("hidden");
}

function toggleTheme() {
    document.body.classList.toggle("dark-mode");
}
