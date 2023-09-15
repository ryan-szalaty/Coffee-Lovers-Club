const frothingButton = document.getElementById("frothing");
const espressoButton = document.getElementById("espresso");
const espressoSection =  document.querySelector(".coffee-tips-espresso");
const frothingSection = document.querySelector(".coffee-tips-froth");
const clickToLearn = document.getElementById("click-to-learn");

const menuToggle = document.querySelector(".menu-toggle");
const menu = document.querySelector(".menu");
const overlay = document.querySelector(".overlay");

function closeMenu() {
    menu.classList.remove("show-menu");
    overlay.classList.remove("show-overlay");
}

overlay.addEventListener("click", (event) => {
    if (event.target === overlay) {
        closeMenu();
    }
});

if (frothingButton && espressoButton) {
    frothingButton.addEventListener("click", () => {
        frothingSection.classList.add("on");
        frothingSection.classList.remove("off");
        espressoSection.classList.add("off");
        espressoSection.classList.remove("on");
    });
    
    espressoButton.addEventListener("click", () => {
        espressoSection.classList.add("on");
        espressoSection.classList.remove("off");
        frothingSection.classList.add("off");
        frothingSection.classList.remove("on");
    });
}

menuToggle.addEventListener("click", () => {
    menu.classList.toggle("show-menu");
    overlay.classList.toggle("show-overlay");
});

menu.querySelectorAll("a").forEach((item) => {
    item.addEventListener("click", () => {
        menu.classList.remove("show-menu");
        overlay.classList.remove("show-overlay");
    });
});
