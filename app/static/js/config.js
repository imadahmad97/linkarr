function addField(containerId, templateId) {
  var container = document.getElementById(containerId);
  var template = document.getElementById(templateId);
  var newField = template.cloneNode(true);
  newField.style.display = "flex";
  newField.removeAttribute("id");
  container.insertBefore(newField, container.querySelector(".add-button"));
}

function removeField(button) {
  var field = button.parentElement;
  field.parentElement.removeChild(field);
}
