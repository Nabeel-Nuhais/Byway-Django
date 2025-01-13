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
});
