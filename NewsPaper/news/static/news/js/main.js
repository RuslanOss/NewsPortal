function toggleMenu(){var n=document.querySelector(".nav-links");n.classList.toggle("show")}
document.addEventListener("click",function(e){var n=document.querySelector(".nav-links");if(!e.target.closest(".navbar"))n.classList.remove("show")});
document.querySelectorAll('a[href^="#"]').forEach(function(a){a.addEventListener("click",function(e){e.preventDefault();var t=document.querySelector(this.getAttribute("href"));if(t)t.scrollIntoView({behavior:"smooth"})})});
document.querySelectorAll(".card").forEach(function(c){c.addEventListener("click",function(e){if(e.target.tagName!=="A"){var r=document.createElement("span");r.className="ripple";var rect=this.getBoundingClientRect();r.style.left=(e.clientX-rect.left)+"px";r.style.top=(e.clientY-rect.top)+"px";this.appendChild(r);setTimeout(function(){r.remove()},600)}})});
console.log("NewsPortal loaded");
