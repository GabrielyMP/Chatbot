chatElement = document.getElementById('chat');
messageElement = document.getElementById('message');
buttonElement = document.getElementById('send');

function createMessageBalloon(content, direction) {
    const messageBalloon = document.createElement('div');
    const messageBalloonContent = document.createTextNode(content);
    
    for(className of ['message-balloon', direction]) {
        messageBalloon.classList.add(className);
    }

    messageBalloon.appendChild(messageBalloonContent);

    return messageBalloon;
}

function addUserResponse(content) {
    const messageWrapper = chatElement.children[0];
    
    const messageBalloon = createMessageBalloon(content, 'right');

    messageWrapper.appendChild(messageBalloon);
}

function addBotResponse(content) {
    const messageWrapper = chatElement.children[0];
    
    const messageBalloon = createMessageBalloon(content, 'left');

    messageWrapper.appendChild(messageBalloon);
}

function scrollDownToLast() {
    const messages = document.querySelectorAll('.message-balloon');

    const lastMessage = messages[messages.length - 1];

    chatElement.scrollTop = lastMessage.offsetTop;
}

buttonElement.addEventListener('click', function(e) {
    const content = messageElement.value;

    if(content == '') {
        console.log('messageElement is empty');
        return;
    }

    addUserResponse(content);


    fetch('http://namaria-chatbot.herokuapp.com/', { 
        method: 'POST', 
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content })
    })
    .then(res => res.json())
    .then(data => {
        if(data.content == 'BUSCAR COORDENADAS') {
            if(navigator.geolocation) {
                let coordinates;

                navigator.geolocation.getCurrentPosition(position => {
                    coordinates = position.coords.latitude + ' ' + position.coords.longitude

                    fetch('http://namaria-chatbot.herokuapp.com/', {
                        method: 'POST',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ content: 'API SENDING USER COORDINATES', coordinates: coordinates })
                    })
                    .then(res => res.json())
                    .then(data => {
                        addBotResponse(data.content);
                        scrollDownToLast();
                    });
                });
            }
            else {
                addBotResponse("Desculpe. O seu browser não suporta geolocalização.")
                scrollDownToLast();
            }
        }
        else {
            addBotResponse(data.content);
            scrollDownToLast();
        }
    });

    messageElement.value = '';
});
