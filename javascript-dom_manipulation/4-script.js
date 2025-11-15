let ul = document.querySelector(".my_list")
const addItem = document.querySelector("#add_item")

const item = '<li>Item</li>';

addItem.addEventListener("click", () => {
    ul.innerHTML += item;
})