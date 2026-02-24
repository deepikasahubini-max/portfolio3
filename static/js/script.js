const sections = ['hero', 'about', 'skills', 'education', 'contact'];
let currentSectionIndex = 0;

function showSection(id) {
    // Update active section
    document.querySelectorAll('.game-section').forEach(s => s.classList.remove('active'));
    document.getElementById(id).classList.add('active');

    // Update active button
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    document.querySelector(`[onclick="showSection('${id}')"]`).classList.add('active');

    currentSectionIndex = sections.indexOf(id);
}

// Keyboard Navigation
document.addEventListener('keydown', (e) => {
    if (document.activeElement.tagName === 'INPUT') return;

    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        currentSectionIndex = (currentSectionIndex + 1) % sections.length;
        showSection(sections[currentSectionIndex]);
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        currentSectionIndex = (currentSectionIndex - 1 + sections.length) % sections.length;
        showSection(sections[currentSectionIndex]);
    }
});

// Chatbot Logic
function toggleChat() {
    const container = document.getElementById('chatbot-container');
    const toggleBtn = document.querySelector('.toggle-btn');
    container.classList.toggle('minimized');
    toggleBtn.textContent = container.classList.contains('minimized') ? '▲' : '▼';
}

function handleKey(e) {
    if (e.key === 'Enter') sendMessage();
}

async function sendMessage() {
    const input = document.getElementById('user-input');
    const msg = input.value.trim();
    if (!msg) return;

    appendMessage('user', msg);
    input.value = '';

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: msg })
        });
        const data = await response.json();
        appendMessage('bot', data.reply);
    } catch (err) {
        appendMessage('bot', 'Oops! The Temple signal is weak. Try again.');
    }
}

function appendMessage(sender, text) {
    const chatMsgs = document.getElementById('chat-messages');
    const msgDiv = document.createElement('div');
    msgDiv.className = `msg ${sender}`;
    msgDiv.textContent = text;
    chatMsgs.appendChild(msgDiv);
    chatMsgs.scrollTop = chatMsgs.scrollHeight;
}
