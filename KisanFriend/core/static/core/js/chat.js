console.log("hello");

const ws = new WebSocket("ws://" + window.location.host + "/ws/chat");

ws.onerror = function(e) {
    console.error("WebSocket error:", e);
};

ws.onopen = function(e) {
    console.log(e, "we are connected with server");
};

ws.onmessage = (e) => {
    const messageData = JSON.parse(e.data);

    const botMessage = document.createElement('div');
    botMessage.classList.add('message', 'bot-message');

    // Add bot logo
    const botLogo = document.createElement('i');
    botLogo.className = "fa-brands fa-rocketchat";
    botMessage.appendChild(botLogo);

    
    botMessage.appendChild(document.createTextNode(`${messageData.message}`));
    document.getElementById('messages').appendChild(botMessage);
    console.log(messageData, "we received message from server");

    if (isAutoSpeak) {
        speakText(messageData.message);
    }
};

ws.onclose = (e) => {
    console.log("Connection closed:", e);
};


const micButton = document.getElementById('mic-button');
const speakerButton = document.getElementById('speaker-button');
const userInput = document.getElementById('user-input');

let recognition;
let isRecording = false;
let isSpeaking = false;
let synth = window.speechSynthesis;
let utterance;
let isAutoSpeak = false;


if ('webkitSpeechRecognition' in window) {
    recognition = new webkitSpeechRecognition();
} else if ('SpeechRecognition' in window) {
    recognition = new SpeechRecognition();
} else {
    console.warn('Speech recognition not supported in this browser.');
}

if (recognition) {
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-IN';

    recognition.onstart = () => {
        isRecording = true;
        micButton.textContent = '🛑'; 
        micButton.title = "Stop Voice Input";
    };

    recognition.onend = () => {
        isRecording = false;
        micButton.textContent = '🎤'; 
        micButton.title = "Start Voice Input";
    };

    recognition.onerror = (event) => {
        console.error("Speech recognition error", event.error);
        recognition.stop();
    };

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        userInput.value = transcript;
        userInput.focus();
    };
}


micButton.addEventListener('click', () => {
    if (!recognition) return;

    if (isRecording) {
        recognition.stop();
    } else {
        recognition.start();
        stopSpeaking(); 
    }
});


function stopSpeaking() {
    if (isSpeaking) {
        synth.cancel();
        isSpeaking = false;
        speakerButton.textContent = '🔊';
        speakerButton.title = "Play Audio";
    }
}


function getIndianMaleVoice() {
    const voices = synth.getVoices();
    return voices.find(voice =>
        voice.lang === 'en-IN' &&
        (voice.name.toLowerCase().includes('male') || voice.name.toLowerCase().includes('google'))
    );
}


function speakText(text) {
    if (isSpeaking) {
        stopSpeaking();
    }

    if (!text) return;

    utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-IN';
    utterance.rate = 1.0; 
    utterance.pitch = 1.0; 
    utterance.voice = getIndianMaleVoice() || null;

    utterance.onstart = () => {
        isSpeaking = true;
        speakerButton.textContent = '⏹️'; 
        speakerButton.title = "Stop Audio";
    };

    utterance.onend = () => {
        isSpeaking = false;
        speakerButton.textContent = '🔊';
        speakerButton.title = "Play Audio";
    };

    utterance.onerror = (e) => {
        console.error('Speech synthesis error', e);
        isSpeaking = false;
        speakerButton.textContent = '🔊';
        speakerButton.title = "Play Audio";
    };

    synth.speak(utterance);
}

speakerButton.addEventListener('click', () => {
    if (isSpeaking) {
        stopSpeaking();
        isAutoSpeak = false; 
    } else {
    
        const messages = document.getElementById('messages');
        const botMessages = messages.querySelectorAll('.bot-message');
        if (botMessages.length === 0) return;

        const lastBotMessage = botMessages[botMessages.length - 1].textContent;
        isAutoSpeak = true;
        speakText(lastBotMessage);
    }
});

function sendMessage(message) {
    if (isSpeaking) {
        stopSpeaking();
    }

    if (typeof message === 'string') {
        ws.send(JSON.stringify({ message }));
    } else if (message instanceof HTMLElement) {
        ws.send(JSON.stringify({ message: message.textContent }));
    }
}

document.getElementById('send-button').addEventListener('click', function() {
    const messageText = userInput.value.trim();

    if (messageText) {
        // Display user message
        const userMessage = document.createElement('div');
        userMessage.classList.add('message', 'user-message');
        userMessage.textContent = messageText;
        document.getElementById('messages').appendChild(userMessage);
console.log("User message sent:", messageText);
        sendMessage(messageText);
        userInput.value = '';
    }
});
