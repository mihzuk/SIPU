let productos = [
  { id: 1, nombre: "Laptop Dell XPS 15", cat: "Electronica", stock: 12, min: 5, precio: 4500000, icon: "💻" },
  { id: 2, nombre: "Monitor Samsung 27\"", cat: "Electronica", stock: 3, min: 5, precio: 1200000, icon: "🖥️" },
  { id: 3, nombre: "Mouse Logitech MX", cat: "Electronica", stock: 25, min: 10, precio: 280000, icon: "🖱️" },
  { id: 4, nombre: "Teclado Mecanico", cat: "Electronica", stock: 0, min: 5, precio: 350000, icon: "⌨️" },
  { id: 5, nombre: "Cafe Premium 500g", cat: "Alimentos", stock: 48, min: 20, precio: 25000, icon: "☕" },
  { id: 6, nombre: "Arroz Diana 5kg", cat: "Alimentos", stock: 7, min: 15, precio: 18000, icon: "🌾" },
  { id: 7, nombre: "Acetaminofen 500mg", cat: "Medicamentos", stock: 120, min: 50, precio: 5000, icon: "💊" },
  { id: 8, nombre: "Camisa Oxford Blanca", cat: "Ropa", stock: 0, min: 3, precio: 85000, icon: "👕" },
];

let movimientos = [
  { id: 1001, prod: "Laptop Dell XPS 15", tipo: "entrada", qty: 5, fecha: "2025-04-28", nota: "Recepcion proveedor" },
  { id: 1002, prod: "Monitor Samsung 27\"", tipo: "salida", qty: 2, fecha: "2025-04-28", nota: "Venta cliente" },
  { id: 1003, prod: "Mouse Logitech MX", tipo: "entrada", qty: 10, fecha: "2025-04-27", nota: "" },
  { id: 1004, prod: "Teclado Mecanico", tipo: "salida", qty: 3, fecha: "2025-04-27", nota: "Venta al por mayor" },
  { id: 1005, prod: "Cafe Premium 500g", tipo: "entrada", qty: 24, fecha: "2025-04-26", nota: "" },
];

const iconsByCat = {
  Electronica: "💻",
  Alimentos: "🥫",
  Ropa: "👕",
  Medicamentos: "💊",
  Herramientas: "🔧",
  Otros: "📦",
};

function showPage(pageId, el) {
  document.querySelectorAll(".page").forEach((p) => p.classList.remove("active"));
  document.querySelectorAll(".nav-item").forEach((n) => n.classList.remove("active"));
  const page = document.getElementById("page-" + pageId);
  if (page) page.classList.add("active");
  if (el) el.classList.add("active");

  const titles = {
    dashboard: ["Dashboard Principal", "Bienvenido al Sistema de Inventario Productivo Universal"],
    inventario: ["Inventario", "Control de stock y productos"],
    productos: ["Catalogo de Productos", "Gestion de productos registrados"],
    ordenes: ["Ordenes de Movimiento", "Historial de entradas y salidas"],
    reportes: ["Reportes y Analisis", "Genera informes detallados de tu negocio"],
    usuarios: ["Gestion de Usuarios", "Administra los accesos al sistema"],
    config: ["Configuracion", "Personaliza SIPU para tu negocio"],
  };
  const t = titles[pageId] || ["SIPU", ""];
  document.getElementById("pageTitle").textContent = t[0];
  document.getElementById("pageSubtitle").textContent = t[1];

  if (pageId === "inventario") renderInventario();
  if (pageId === "productos") renderProductos();
  if (pageId === "ordenes") renderOrdenes();
}

function getEstado(prod) {
  if (prod.stock === 0) return { label: "Agotado", cls: "stock-out", key: "out" };
  if (prod.stock < prod.min) return { label: "Stock Bajo", cls: "stock-low", key: "low" };
  return { label: "Disponible", cls: "stock-ok", key: "ok" };
}

let currentFilter = "all";

function renderInventario(filter) {
  if (filter !== undefined) currentFilter = filter;
  const body = document.getElementById("inventarioBody");
  let list = productos;
  if (currentFilter !== "all") list = productos.filter((p) => getEstado(p).key === currentFilter);
  body.innerHTML =
    list
      .map((p) => {
        const est = getEstado(p);
        return `<tr>
      <td><div style="display:flex;align-items:center;gap:8px;"><span style="font-size:18px;">${p.icon}</span><span style="font-weight:500;">${p.nombre}</span></div></td>
      <td style="color:var(--gray-500);font-size:12px;">${p.cat}</td>
      <td><strong>${p.stock}</strong></td>
      <td style="color:var(--gray-500);">${p.min}</td>
      <td>$${p.precio.toLocaleString()}</td>
      <td>$${(p.stock * p.precio).toLocaleString()}</td>
      <td><span class="stock-badge ${est.cls}">${est.label}</span></td>
      <td><span class="action-dots" onclick="showToast('Opciones para: ${p.nombre}', 'info')">⋯</span></td>
    </tr>`;
      })
      .join("") ||
    `<tr><td colspan="8" class="empty-state"><div class="empty-icon">📦</div><p>No hay productos con este filtro</p></td></tr>`;
}

function filterTable(f, el) {
  document.querySelectorAll(".filter-chips .chip").forEach((c) => c.classList.remove("active"));
  el.classList.add("active");
  renderInventario(f);
}

function searchTable(q) {
  const tbody = document.getElementById("inventarioBody");
  if (!q) {
    renderInventario();
    return;
  }
  const list = productos.filter(
    (p) => p.nombre.toLowerCase().includes(q.toLowerCase()) || p.cat.toLowerCase().includes(q.toLowerCase())
  );
  tbody.innerHTML =
    list
      .map((p) => {
        const est = getEstado(p);
        return `<tr>
      <td><div style="display:flex;align-items:center;gap:8px;"><span>${p.icon}</span><span style="font-weight:500;">${p.nombre}</span></div></td>
      <td style="color:var(--gray-500);font-size:12px;">${p.cat}</td>
      <td><strong>${p.stock}</strong></td>
      <td style="color:var(--gray-500);">${p.min}</td>
      <td>$${p.precio.toLocaleString()}</td>
      <td>$${(p.stock * p.precio).toLocaleString()}</td>
      <td><span class="stock-badge ${est.cls}">${est.label}</span></td>
      <td><span class="action-dots">⋯</span></td>
    </tr>`;
      })
      .join("") ||
    `<tr><td colspan="8" style="text-align:center;padding:32px;color:var(--gray-500);">Sin resultados para "${q}"</td></tr>`;
}

function renderProductos() {
  const grid = document.getElementById("productsGrid");
  grid.innerHTML = productos
    .map((p) => {
      const est = getEstado(p);
      return `<div class="prod-card" onclick="showToast('Editando: ${p.nombre}', 'info')">
      <div class="prod-img">${p.icon}</div>
      <div class="prod-info">
        <div class="prod-name">${p.nombre}</div>
        <div class="prod-cat">${p.cat}</div>
        <div class="prod-meta">
          <div class="prod-price">$${p.precio.toLocaleString()}</div>
          <div class="prod-stock"><span class="stock-badge ${est.cls}">${p.stock} uds</span></div>
        </div>
      </div>
    </div>`;
    })
    .join("");
}

function renderOrdenes() {
  const body = document.getElementById("ordenesBody");
  body.innerHTML = movimientos
    .map((m) => {
      const esEntrada = m.tipo === "entrada";
      const tipoCls = esEntrada ? "stock-ok" : m.tipo === "salida" ? "stock-out" : "stock-low";
      const tipoLabel = m.tipo.charAt(0).toUpperCase() + m.tipo.slice(1);
      return `<tr>
      <td style="font-family:Syne,sans-serif;font-weight:700;">#${m.id}</td>
      <td>${m.prod}</td>
      <td><span class="stock-badge ${tipoCls}">${tipoLabel}</span></td>
      <td><strong style="color:${esEntrada ? "var(--green)" : "var(--red)"};">${esEntrada ? "+" : "-"}${m.qty}</strong></td>
      <td style="color:var(--gray-500);font-size:12px;">${m.fecha}</td>
      <td><span class="stock-badge stock-ok">Completado</span></td>
      <td><span class="action-dots">⋯</span></td>
    </tr>`;
    })
    .join("");
}

function updateProductSelect() {
  const sel = document.getElementById("mProducto");
  sel.innerHTML =
    '<option value="">Seleccionar...</option>' +
    productos.map((p) => `<option value="${p.id}">${p.nombre}</option>`).join("");
}

function openModal(id) {
  document.getElementById(id).classList.add("open");
  if (id === "modalMovimiento") {
    updateProductSelect();
    document.getElementById("mFecha").value = new Date().toISOString().split("T")[0];
  }
}

function closeModal(id) {
  document.getElementById(id).classList.remove("open");
}

document.querySelectorAll(".modal-overlay").forEach((m) => {
  m.addEventListener("click", (e) => {
    if (e.target === m) m.classList.remove("open");
  });
});

function guardarProducto() {
  const nombre = document.getElementById("pNombre").value.trim();
  const cat = document.getElementById("pCategoria").value;
  const stock = parseInt(document.getElementById("pStock").value) || 0;
  const min = parseInt(document.getElementById("pStockMin").value) || 10;
  const precio = parseFloat(document.getElementById("pPrecio").value) || 0;

  if (!nombre || !cat) {
    showToast("Completa los campos requeridos", "error");
    return;
  }

  productos.push({ id: Date.now(), nombre, cat, stock, min, precio, icon: iconsByCat[cat] || "📦" });

  document.getElementById("pNombre").value = "";
  document.getElementById("pCategoria").value = "";
  document.getElementById("pStock").value = "";
  document.getElementById("pStockMin").value = "";
  document.getElementById("pPrecio").value = "";

  closeModal("modalProducto");
  showToast(`✓ "${nombre}" agregado al inventario`, "success");

  document.getElementById("kpi-productos").textContent = (2847 + productos.length - 8).toLocaleString();

  renderInventario();
  renderProductos();
}

function registrarMovimiento() {
  const tipo = document.getElementById("mTipo").value;
  const prodId = document.getElementById("mProducto").value;
  const qty = parseInt(document.getElementById("mCantidad").value);
  const fecha = document.getElementById("mFecha").value;
  const nota = document.getElementById("mNota").value;

  if (!prodId || !qty || qty <= 0) {
    showToast("Completa todos los campos requeridos", "error");
    return;
  }

  const prod = productos.find((p) => p.id == prodId);
  if (!prod) return;

  if (tipo === "salida" && qty > prod.stock) {
    showToast(`Stock insuficiente. Disponible: ${prod.stock} unidades`, "error");
    return;
  }

  if (tipo === "entrada") prod.stock += qty;
  else if (tipo === "salida") prod.stock -= qty;

  const mov = {
    id: Date.now(),
    prod: prod.nombre,
    tipo,
    qty,
    fecha: fecha || new Date().toISOString().split("T")[0],
    nota,
  };
  movimientos.unshift(mov);

  const movList = document.getElementById("movList");
  const dot = tipo === "entrada" ? "in" : "out";
  const sign = tipo === "entrada" ? "+" : "-";
  const newItem = document.createElement("div");
  newItem.className = "mov-item";
  newItem.innerHTML = `<div class="mov-dot ${dot}"></div><div class="mov-info"><div class="mov-name">${prod.nombre}</div><div class="mov-time">Ahora mismo</div></div><div class="mov-qty ${dot}">${sign}${qty}</div>`;
  movList.prepend(newItem);
  if (movList.children.length > 5) movList.lastChild.remove();

  closeModal("modalMovimiento");
  showToast(`✓ Movimiento registrado — ${prod.nombre} ${sign}${qty}`, "success");
  renderInventario();
}

function handleSearch(q) {
  if (!q) return;
  showToast(`Buscando: "${q}"`, "info");
}

function showToast(msg, type = "info") {
  const icons = { success: "✅", error: "❌", info: "ℹ️" };
  const t = document.createElement("div");
  t.className = `toast ${type}`;
  t.innerHTML = `<span>${icons[type]}</span><span>${msg}</span>`;
  document.getElementById("toastContainer").prepend(t);
  setTimeout(() => t.remove(), 3500);
}

document.querySelectorAll(".bar").forEach((b) => {
  b.addEventListener("mouseenter", function () {
    document.querySelectorAll(".bar").forEach((x) => x.classList.remove("active"));
    this.classList.add("active");
  });
});

document.addEventListener("DOMContentLoaded", () => {
  renderInventario();
  renderProductos();
  renderOrdenes();
  updateProductSelect();
});
