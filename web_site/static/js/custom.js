$(document).ready(function () {
    $('.languages').select2({
        minimumResultsForSearch: Infinity,
        containerCssClass: "error",
        dropdownCssClass: "test"
    });
});

const commentsCarousel = document.getElementById("comments_carousel");

Fancybox.bind(commentsCarousel, "[data-fancybox]", {});




// function sendPostRequest() {
//     var url = 'http://127.0.0.1:8000/sizes/'; // Замените на URL вашего сервера или API
//     var params = {
//         param1: 'value1',
//         param2: 'value2'
//     };
//
//     fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(params)
//     })
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             return response.text();
//         })
//         .then(data => {
//             // Обработка ответа сервера
//             console.log(data);
//         })
//         .catch(error => {
//             // Обработка ошибок
//             console.error('There has been a problem with your fetch operation:', error);
//         });
// }
//
// sendPostRequest()


// let authButton = document.querySelector('[data-auth]');
// let modal = document.querySelector('.modal');
//
// authButton.addEventListener('click', () => {
//     modal.classList.add('active', 'zIndex');
//     document.body.style.overflow = 'hidden'
// });
