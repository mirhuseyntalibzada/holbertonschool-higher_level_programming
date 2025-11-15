const character = document.querySelector("#character")

const fetchData = async () => {
    const res = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
    const data = await res.json();

    character.innerHTML = data.name;
}

fetchData();