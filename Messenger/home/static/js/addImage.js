const imageDivList = document.getElementsByClassName("add-image");
// const sendImageButtonList = document.getElementsByClassName("addImageButton");
const addImageInputList = document.getElementsByClassName("addImageInput");

const showImageDivList = document.getElementsByClassName("post-image");
const tempContainer = document.getElementsByClassName("temp-image-container");

for (let addImageInput of addImageInputList){
    addImageInput.addEventListener("change", ()=>{
        let formData = new FormData();
        imageData = addImageInput.files[0]
        formData.append('image', imageData);
        console.log("data =", formData, document.cookie.split("csrftoken=")[1].split(";")[0]);
        $.ajax({
            url: 'load_image/',
            type: "post",
            data: formData,
            contentType: false,
            processData: false,
            headers: {'X-CSRFToken': document.cookie.split("csrftoken=")[1].split(";")[0]},
        })
        showImage(imageData)
    })
}

function showImage(image){
    let imageElement = document.createElement("div");
    const getSizeImg = new Image();
    url = `http://127.0.0.1:8000/media/post_images/${image.name}`;
    console.log("url =", url);
    // getSizeImg. = `url('${url}')`;
    imageElement.style.backgroundImage = `url('${url}')`;
    const width = getSizeImg.naturalWidth;
    const height = getSizeImg.naturalHeight;
    console.log(width, height);
    if (width > height){
        imageElement.classList.add('horizontal-image');
    } else{
        imageElement.classList.add('vertical-image');
    }
    imageElement.style.backgroundImage = url;
    console.log("temp cont =", tempContainer);
    tempContainer[0].appendChild(imageElement);
}