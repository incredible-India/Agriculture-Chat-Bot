document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input');
    const messageText = userInput.value;

    if (messageText) {
        // Display user message
        const userMessage = document.createElement('div');
        userMessage.classList.add('message', 'user-message');
        userMessage.textContent = messageText;
        document.getElementById('messages').appendChild(userMessage);
        userInput.value = '';

        // Simulate bot reply
        setTimeout(() => {
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot-message');

            // Add bot logo
            const botLogo = document.createElement('i');
            botLogo.class = "fa-brands fa-rocketchat"; // Replace with your bot logo path
            botMessage.appendChild(botLogo);

            // Add bot reply text
            botMessage.appendChild(document.createTextNode("Hello! How can I assist you today?"));
            document.getElementById('messages').appendChild(botMessage);
        }, 1000);
    }
});