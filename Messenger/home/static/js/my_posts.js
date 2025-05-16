console.log("myposts.js loaded");

function toggleMenu(postId) {
    const menu = document.getElementById(`menu-${postId}`);
    const allMenus = document.querySelectorAll('.dropdown-menu');

    allMenus.forEach(m => {
        if (m !== menu) {
            m.style.display = "none";
        }
    });

    const currentDisplay = window.getComputedStyle(menu).display;
    menu.style.display = (currentDisplay === "none") ? "block" : "none";
}

window.addEventListener("click", function(e) {
    if (!e.target.closest(".dots")) {
        document.querySelectorAll(".dropdown-menu").forEach(menu => {
            menu.style.display = "none";
        });
    }
});

document.querySelectorAll(".dropdown-menu").forEach(menu => {
    menu.addEventListener("click", function(e) {
        e.stopPropagation();
    });
});
