const a=document.getElementById("frothing"),e=document.getElementById("espresso"),t=document.querySelector(".coffee-tips-espresso"),n=document.querySelector(".coffee-tips-froth"),c=document.getElementById("click-to-learn");a.addEventListener("click",()=>{n.classList.add("on"),n.classList.remove("off"),t.classList.add("off"),t.classList.remove("on")}),e.addEventListener("click",()=>{t.classList.add("on"),t.classList.remove("off"),n.classList.add("off"),n.classList.remove("on")});