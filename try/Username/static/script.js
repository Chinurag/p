function handleUsernameFocus(input) {
    input.value = "@";
    input.placeholder = "Username";
}

function handleUsernameBlur(input) {
    if (input.value === "@") {
        input.value = "";
        input.placeholder = "Enter Instagram Username";
    }
}
