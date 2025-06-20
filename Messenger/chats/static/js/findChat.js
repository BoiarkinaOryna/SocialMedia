// const input = document.querySelector("input[name='message']");
// console.log("input =", input);
// const button = document.getElementById("#sendMessage");

// button.addEventListener("click", ()=>{
//     let formData = new FormData();
//     formData.append(input.value);
//     $.ajax({
//         url: `/friends/${type}/`,
//         type: "post",
//         data: formData,
//         contentType: false,
//         processData: false,
//         headers: {'X-CSRFToken': document.cookie.split("csrftoken=")[1].split(";")[0]},
//         success: function(){$(".main-block").load(window.location.href + " .main-block > *")}
//     })
// })

let groupPk = 1

const webSocket = new WebSocket(`ws://${window.location.host}/chat/${groupPk}`)

let messageForm = document.querySelector('#message')
// Додаємо подію до форми
messageForm.addEventListener(
    type = 'submit',
    (event) =>{
        // Прибираэмо стан форми за замовчуванням, щоб вона не відправлялась
        event.preventDefault();
        // Отримуємо значення повідомлення
        let data_message = event.target.message.value;
        // Відправляємо повідомлення на сервер у форматі json
        webSocket.send(JSON.stringify({
            'message': data_message
        }));
    }
)
