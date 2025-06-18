let buttonList = document.getElementsByClassName("confirm-button");
const mainBlock = document.querySelector(".main-block");

for(let button of buttonList){
    button.addEventListener("click", ()=>{

        let formData = new FormData();
        formData.append('user_id', button.id);
        console.log("data =", formData);
        let type = button.value;
        console.log("type =", type)
        $.ajax({
            url: `/friends/${type}/`,
            type: "post",
            data: formData,
            contentType: false,
            processData: false,
            headers: {'X-CSRFToken': document.cookie.split("csrftoken=")[1].split(";")[0]},
            // success: function(response){mainBlock.load(`/friends/${type}/`)}
            success: $(".main-block").load(window.location.href + " .main-block > *")
        })
    })
}