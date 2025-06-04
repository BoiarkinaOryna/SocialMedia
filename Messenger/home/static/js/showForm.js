const showCreatePost = document.getElementById("createPublication");
const showChangePost = document.querySelectorAll(".showChangePost");
const formCreate = document.getElementById("create");
const formChangeList = document.querySelectorAll(".changePostForm");
const main = document.querySelector("main");
const header = document.querySelector("header");
const body = document.querySelector("body");
const myInfo = document.querySelector(".my-info");
const feed = document.querySelector(".social-media-feed");
const closeButtonList = document.querySelectorAll("#closePostForm");
const darkBackgrond = document.querySelector(".dark-background");

let buttonList = [showCreatePost];

if (showChangePost != null){
    for (let item of showChangePost){
        buttonList.push(item);
    }
}
let formList = [formCreate];

console.log("formList1 =", formList);
if (formChangeList != null){
    for (let element of formChangeList){
        formList.push(element);
    } 
}
console.log("formList2 =", formList);

for (let button of buttonList){
    button.addEventListener("click", ()=>{
        console.log("formList =", formList);
        darkBackgrond.classList.add("active-dark-background");
        for (form of formList){
            if (form.id == "create"){
                // console.log("button (create) id =", button.id)
                if (button.id == "createPublication"){
                    form.classList.add("post-form");
                    form.classList.remove("hidden-post-form");
                }
            } else{
                // for (let oneForm of form){
                let oneForm = form;
                    console.log("oneForm =", oneForm.id);
                    console.log("button.id", button.id);
                    if (oneForm.id == `change${button.id}`){
                        console.log("1");
                        form.classList.add("post-form");
                        form.classList.remove("hidden-post-form");
                    }
                // }
            }
        }

    });
}

for (let closeButton of closeButtonList){
    console.log("closeButton", closeButton)
    closeButton.addEventListener("click", ()=>{
        for (form of formList){
            if (!form.classList.contains("hidden-post-form")){
                form.classList.add("hidden-post-form");
            }
            form.classList.remove("post-form");
        }
        darkBackgrond.classList.remove("active-dark-background");
    });
}