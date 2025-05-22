// On page load, immediately apply dark mode if user previously enabled it
document.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("darkMode") === "enabled") {
    document.body.classList.add("dark-mode");
  }
});

// Called when the user clicks the toggle button
function switchBetweenDarkAndLightMode() {
  document.body.classList.toggle("dark-mode");
  if (document.body.classList.contains("dark-mode")) {
    localStorage.setItem("darkMode", "enabled");
  } else {
    localStorage.setItem("darkMode", "disabled");
  }
}
