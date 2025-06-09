const imageDivList = document.getElementsByClassName("add-image");
// const sendImageButtonList = document.getElementsByClassName("addImageButton");
const addImageInputList = document.getElementsByClassName("addImageInput");

for (let addImageInput of addImageInputList){
    addImageInput.addEventListener("change", ()=>{
        let formData = new FormData();
        let file = addImageInput.files[0];
        formData.append('image', $('.addImageInput')[0].file);
        console.log("data =", formData, document.cookie.split("csrftoken=")[1].split(";")[0]);
        $.ajax({
            url: 'load_image/',
            type: "post",
            data: formData,
            contentType: false,
            processData: false,
            headers: {'X-CSRFToken': document.cookie.split("csrftoken=")[1].split(";")[0]},
        })
    })
}