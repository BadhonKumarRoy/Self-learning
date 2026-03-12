function changeText() {
    const textElement = document.getElementById("changeText");
    if(textElement.innerHTML === "JavaScript can change HTML content!") {
        textElement.innerHTML = "Hello JavaScript!";
    } else {
        textElement.innerHTML = "JavaScript can change HTML content!";
    }
}