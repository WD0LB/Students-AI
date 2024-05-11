function showNext(page) {
    document.getElementById("page" + page).classList.remove("active");
    document.getElementById("page" + (page + 1)).classList.add("active");
}

function showPrevious(page) {
    document.getElementById("page" + page).classList.remove("active");
    document.getElementById("page" + (page - 1)).classList.add("active");
}

document.getElementById("predictionForm").addEventListener("submit", function(event){
    var input = document.getElementById("npt").value;
    if (!input.match(/^[0-9]+$/)) { // Example: checks if input is numeric
      alert("All inputs should be numeric!");
      event.preventDefault(); // Prevent form submission
    }
  });