// ======================================================
// RailCode Scripts
// Minimal, clean interactions
// ======================================================

window.addEventListener("scroll", function () {
  const navbar = document.getElementById("mainNav");

  if (window.scrollY > 50) {
    navbar.classList.add("shadow-sm");
  } else {
    navbar.classList.remove("shadow-sm");
  }
});