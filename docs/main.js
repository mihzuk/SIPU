const nav = document.querySelector(".nav");
const toggle = document.querySelector(".menu-toggle");
const form = document.querySelector("#contactForm");
const toast = document.querySelector("#toast");

if (toggle) {
  toggle.addEventListener("click", () => {
    nav.classList.toggle("open");
  });
}

function showToast(message, type = "success") {
  if (!toast) return;
  toast.textContent = message;
  toast.className = `toast show ${type}`;
  window.setTimeout(() => {
    toast.className = "toast";
  }, 3200);
}

function setError(field, message) {
  const input = field.querySelector(".form-input");
  const help = field.querySelector(".form-help");
  if (input) input.classList.add("error");
  if (help) help.textContent = message;
}

function clearError(field) {
  const input = field.querySelector(".form-input");
  const help = field.querySelector(".form-help");
  if (input) input.classList.remove("error");
  if (help) help.textContent = "";
}

function isEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}

if (form) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const fields = form.querySelectorAll(".form-group");
    fields.forEach(clearError);

    const name = form.querySelector("#name");
    const email = form.querySelector("#email");
    const company = form.querySelector("#company");
    const message = form.querySelector("#message");

    let valid = true;

    if (!name.value.trim()) {
      setError(name.closest(".form-group"), "Ingresa tu nombre.");
      valid = false;
    }

    if (!email.value.trim() || !isEmail(email.value)) {
      setError(email.closest(".form-group"), "Ingresa un correo valido.");
      valid = false;
    }

    if (!company.value.trim()) {
      setError(company.closest(".form-group"), "Ingresa el nombre del negocio.");
      valid = false;
    }

    if (!message.value.trim() || message.value.trim().length < 12) {
      setError(message.closest(".form-group"), "Describe tu necesidad (minimo 12 caracteres).");
      valid = false;
    }

    if (!valid) {
      showToast("Revisa los campos marcados.", "error");
      return;
    }

    form.reset();
    showToast("Mensaje listo. Te responderemos pronto.", "success");
  });
}
