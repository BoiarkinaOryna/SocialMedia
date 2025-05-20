const button = document.getElementById("createPublication");
const form = document.getElementById("createPostForm");
const main = document.querySelector("main");
const header = document.querySelector("header");
const body = document.querySelector("body");
const myInfo = document.querySelector(".my-info");
const feed = document.querySelector(".social-media-feed");
const closeButton = document.getElementById("closePostForm")

button.addEventListener("click", ()=>{
    console.log("added Event listener");
    form.classList.add("post-form");
    form.classList.remove("hidden-post-form");
    // main.classList.add("dark");
    header.classList.add("dark");
    myInfo.classList.add("dark");
    feed.classList.add("dark");
    body.style.backgroundColor = "#484749";
});

closeButton.addEventListener("click", ()=>{
    form.classList.add("hidden-post-form");
    form.classList.remove("post-form");
    header.classList.remove("dark");
    myInfo.classList.remove("dark");
    feed.classList.remove("dark");
    body.style.backgroundColor = '';
});