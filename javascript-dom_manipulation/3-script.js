const header = document.querySelector("header");
header.className = "green";
const toggleHeader = document.querySelector("#toggle_header");
toggleHeader.addEventListener("click", () => {
    if (header.className === "red") {
        header.className = "green";
    } else {
        header.className = "red";
    }
})
