const optionDivsList = document.querySelectorAll(".post-options");

for (let optionDiv of optionDivsList){
    optionDiv.addEventListener("click", ()=> {
        let id = optionDiv.id;
        let form = document.getElementById(`form-${id}`);
        if (form.classList == "hidden-form"){
            form.classList.remove("hidden-form");
            form.classList.add("visible-form");
        }else if (form.classList == "visible-form"){
            form.classList.add("hidden-form");
            form.classList.remove("visible-form");
        }
    })
}