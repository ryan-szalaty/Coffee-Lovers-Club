const frothingButton = document.getElementById("frothing");
const espressoButton = document.getElementById("espresso");
const espressoSection =  document.querySelector(".coffee-tips-espresso");
const frothingSection = document.querySelector(".coffee-tips-froth");
const clickToLearn = document.getElementById("click-to-learn");

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
})
