document.addEventListener("DOMContentLoaded", () => {
    let hello = document.querySelector("#hello")

    const fetchData = async () => {
        const res = await fetch("https://hellosalut.stefanbohacek.com/?lang=fr");
        const data = await res.json();

        console.log(data.hello);

        hello.textContent = data.hello;
    }

    fetchData();
})