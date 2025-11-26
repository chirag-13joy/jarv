let isMuted = false;
let isListening = false;

const speakBtn = document.getElementById('speakBtn');
const muteBtn = document.getElementById('muteBtn');
const statusText = document.getElementById('statusText');
const listeningIndicator = document.getElementById('listeningIndicator');
const response = document.getElementById('response');
const responseText = document.getElementById('responseText');

// Check server status on load
checkStatus();

function checkStatus() {
    fetch('/api/status')
        .then(res => res.json())
        .then(data => {
            if (data.status === 'online') {
                statusText.textContent = 'System Online';
            }
        })
        .catch(err => {
            statusText.textContent = 'Server Offline';
            console.error('Status check failed:', err);
        });
}

speakBtn.addEventListener('click', () => {
    if (isListening) return;

    isListening = true;
    listeningIndicator.classList.add('active');
    statusText.textContent = 'Listening...';
    speakBtn.textContent = '⏸️ Listening...';
    speakBtn.disabled = true;

    // Call backend API
    fetch('/api/speak', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                response.classList.add('active');
                responseText.textContent = data.message;
            }

            // Simulate listening duration
            setTimeout(() => {
                isListening = false;
                listeningIndicator.classList.remove('active');
                statusText.textContent = 'System Online';
                speakBtn.textContent = '🎤 Speak';
                speakBtn.disabled = false;
            }, 3000);
        })
        .catch(err => {
            console.error('Speak API failed:', err);
            isListening = false;
            listeningIndicator.classList.remove('active');
            statusText.textContent = 'Error - Check Console';
            speakBtn.textContent = '🎤 Speak';
            speakBtn.disabled = false;

            response.classList.add('active');
            responseText.textContent = 'Error connecting to backend. Make sure web_server.py is running.';
        });
});

muteBtn.addEventListener('click', () => {
    isMuted = !isMuted;
    muteBtn.classList.toggle('active');

    // Call backend API
    fetch('/api/mute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ muted: isMuted })
    })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                if (isMuted) {
                    muteBtn.textContent = '🔇 Voice Off';
                    statusText.textContent = 'Silent Mode';
                } else {
                    muteBtn.textContent = '🔊 Voice On';
                    statusText.textContent = 'System Online';
                }
            }
        })
        .catch(err => {
            console.error('Mute API failed:', err);
        });
});

// Add click handlers to example cards for quick testing
document.querySelectorAll('.example-card').forEach(card => {
    card.addEventListener('click', () => {
        const commandText = card.querySelector('span').textContent;
        testCommand(commandText);
    });
});

function testCommand(commandText) {
    response.classList.add('active');
    responseText.textContent = 'Processing: ' + commandText;

    fetch('/api/command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ command: commandText })
    })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                responseText.textContent = data.response;
            }
        })
        .catch(err => {
            console.error('Command API failed:', err);
            responseText.textContent = 'Error processing command';
        });
}
