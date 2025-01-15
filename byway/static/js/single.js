document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card-reviews");
  const nextButton = document.querySelector(
    ".swiper-pagination button:last-child"
  );
  const prevButton = document.querySelector(
    ".swiper-pagination button:first-child"
  );

  let currentIndex = 0;

  const updateCardsDisplay = () => {
    cards.forEach((card, index) => {
      if (index >= currentIndex && index < currentIndex + 3) {
        card.classList.add("active");
        card.style.display = "flex";
      } else {
        card.classList.remove("active");
        setTimeout(() => (card.style.display = "none"), 300); // Delay hiding to allow transition
      }
    });
  };

  nextButton.addEventListener("click", () => {
    if (currentIndex + 3 < cards.length) {
      currentIndex += 3;
      updateCardsDisplay();
    }
  });

  prevButton.addEventListener("click", () => {
    if (currentIndex - 3 >= 0) {
      currentIndex -= 3;
      updateCardsDisplay();
    }
  });

  // Initial display
  updateCardsDisplay();

  // active tab
  const tabs = document.querySelectorAll(
    "#course-description .description-top .description"
  );

  tabs.forEach((tab, index) => {
    tab.addEventListener("click", function () {
      // Remove the active state from all tabs
      tabs.forEach((t) => {
        t.style.backgroundColor = "#fff";
        t.style.color = "#0F172A";
      });

      // Set the clicked tab as active
      tab.style.backgroundColor = "#EFF6FF";
    });

    // Set the first tab as active by default
    if (index === 0) {
      tab.style.backgroundColor = "#EFF6FF";
    }
  });
});
