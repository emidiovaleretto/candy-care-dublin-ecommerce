// This event fires as soon as the page loaded.
document.addEventListener("DOMContentLoaded", () => {
  const btnMobile = document.getElementById("btn-mobile");

  // This function handles the click event on the button
  function toggleMenu(event) {
    if (event.type === "touchstart") {
      event.preventDefault();
    }
    const nav = document.getElementById("nav");
    nav.classList.toggle("active");
    const active = nav.classList.contains("active");
    event.currentTarget.setAttribute("aria-expanded", active);

    if (active) {
      event.currentTarget.setAttribute("aria-label", "Close menu");
    } else {
      event.currentTarget.setAttribute("aria-label", "Open menu");
    }
  }

  btnMobile.addEventListener("click", toggleMenu);
  btnMobile.addEventListener("touchstart", toggleMenu);

  // This function handles to get the current year
  $(".current_year").text(new Date().getFullYear());
});
