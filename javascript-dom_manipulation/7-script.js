const ul = document.querySelector("#list_movies")

const fetchData = async () => {
    const res = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
    const data = await res.json();

    let item = ''
    data.results.map((movie) => {
        item = `<li>${movie.title}</li>`
        ul.innerHTML += item;
    });
}

fetchData();