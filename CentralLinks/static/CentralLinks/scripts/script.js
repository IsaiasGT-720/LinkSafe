const addBtn = document.getElementById("addLinkBtn");
  const modal = document.getElementById("modalOverlay");
  const closeBtn = document.getElementById("closeModal");

  addBtn.addEventListener("click", () => {
    modal.style.display = "flex";
  });

  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  modal.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.style.display = "none";
    }
  });