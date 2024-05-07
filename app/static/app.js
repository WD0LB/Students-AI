function showNext(page) {
    document.getElementById("page" + page).classList.remove("active");
    document.getElementById("page" + (page + 1)).classList.add("active");
}

function showPrevious(page) {
    document.getElementById("page" + page).classList.remove("active");
    document.getElementById("page" + (page - 1)).classList.add("active");
}