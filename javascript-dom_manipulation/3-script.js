document.addEventListener("DOMContentLoaded", function () {
    const headerElement = document.querySelector("header");
    const toggleButton = document.getElementById("toggle_header");
  
    toggleButton.addEventListener("click", function () {
      if (headerElement.classList.contains("red")) {
        headerElement.classList.remove("red");
        headerElement.classList.add("green");
      } else if (headerElement.classList.contains("green")) {
        headerElement.classList.remove("green");
        headerElement.classList.add("red");
      }
    });
  });
