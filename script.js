let isMuted = false;
let isListening = false;

const speakBtn = document.getElementById('speakBtn');
const muteBtn = document.getElementById('muteBtn');
const statusText = document.getElementById('statusText');
const listeningIndicator = document.getElementById('listeningIndicator');
const response = document.getElementById('response');
const responseText = document.getElementById('responseText');

speakBtn.addEventListener('click', () => {
    if (isListening) return;
    
    isListening = true;
    listeningIndicator.classList.add('active');
    statusText.textContent = 'Listening...';
    speakBtn.textContent = '⏸️ Listening...';
    speakBtn.disabled = true;

    // Simulate listening (in real implementation, this would call the backend)
    setTimeout(() => {
        isListening = false;
        listeningIndicator.classList.remove('active');
        statusText.textContent = 'System Online';
        speakBtn.textContent = '🎤 Speak';
        speakBtn.disabled = false;
        
        // Show example response
        response.classList.add('active');
        responseText.textContent = 'Command received! (Connect to backend for real responses)';
    }, 3000);
});

muteBtn.addEventListener('click', () => {
    isMuted = !isMuted;
    muteBtn.classList.toggle('active');
    
    if (isMuted) {
        muteBtn.textContent = '🔇 Voice Off';
        statusText.textContent = 'Silent Mode';
    } else {
        muteBtn.textContent = '🔊 Voice On';
        statusText.textContent = 'System Online';
    }
});
