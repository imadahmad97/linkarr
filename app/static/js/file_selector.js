function checkAndSubmit() {
  const source = document.getElementById("source_dir").value;
  const target = document.getElementById("target_dir").value;

  if (source && target) {
    document.forms[0].submit();
  }
}

function toggleButtons() {
  const source = document.getElementById("source_dir").value;
  const target = document.getElementById("target_dir").value;
  const hardBtn = document.getElementById("hardlink_button");
  const symbolicBtn = document.getElementById("symboliclink_button");
  const unlinkBtn = document.getElementById("unlink_button");

  const enable = source && target;
  hardBtn.disabled = !enable;
  symbolicBtn.disabled = !enable;
  unlinkBtn.disabled = !enable;
}

document.getElementById("source_dir").addEventListener("change", toggleButtons);
document.getElementById("target_dir").addEventListener("change", toggleButtons);

function bulkLinkButton(linkType) {
  const form = document.getElementById("bottom-button-form");
  const checkboxes = document.querySelectorAll(".item-checkbox:checked");
  const container = document.getElementById("selected-items-hidden-container");
  container.innerHTML = ""; // Clear previous hidden inputs
  checkboxes.forEach((cb) => {
    const input = document.createElement("input");
    input.type = "hidden";
    input.name = "selected_items";
    input.value = cb.value;
    container.appendChild(input);
  });

  if (linkType === "hard") {
    form.action = URLS.hardlink;
  } else if (linkType === "symbolic") {
    form.action = URLS.symlink;
  } else if (linkType === "unlink") {
    form.action = URLS.unlink;
  }
}

// In case both are pre-filled from a GET request
window.addEventListener("DOMContentLoaded", toggleButtons);

document.addEventListener("DOMContentLoaded", function () {
  toggleButtons(); // Ensure buttons are toggled correctly on load

  const items = Array.from(document.querySelectorAll(".searchable-item"));
  const fuseData = items.map((item) => ({
    el: item,
    name: item.dataset.name,
  }));

  const fuse = new Fuse(fuseData, {
    keys: ["name"],
    threshold: 0.4, // 0.0 is exact match, 1.0 is match everything — 0.4 is good default
    ignoreLocation: true,
  });

  const searchInput = document.getElementById("searchInput");
  searchInput.addEventListener("input", function () {
    const query = this.value.trim();

    // Reset all items
    items.forEach((item) => (item.style.display = "none"));

    // If no query, show all
    if (!query) {
      items.forEach((item) => (item.style.display = ""));
      return;
    }

    // Get Fuse.js results
    const results = fuse.search(query).map((r) => r.item.el);

    // Show only matched items
    results.forEach((item) => (item.style.display = ""));
  });
});
