chatElement = document.getElementById('chat');
messageElement = document.getElementById('message');
buttonElement = document.getElementById('send');

buttonElement.addEventListener('click', function(e) {
    console.log('Send message');

    const messageContent = messageElement.value;

    if(messageContent == '') {
        console.log('messageElement is empty');
        return;
    }

    const request = new Request('http://localhost:5000/');
    request.method = 'POST';

    fetch(request)
    .then(response => {
        console.log('recebeu');
        console.log(response.json())
    })
    .catch(err => console.log(err));

    messageElement.value = '';
});


