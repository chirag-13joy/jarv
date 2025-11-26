from flask import Flask, render_template, jsonify, request
import os
import threading
import queue

app = Flask(__name__, template_folder='.')

# Global state
voice_enabled = True
command_queue = queue.Queue()
response_queue = queue.Queue()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'online',
        'voice_enabled': voice_enabled
    })

@app.route('/api/speak', methods=['POST'])
def speak():
    """Trigger voice listening"""
    try:
        # In a real implementation, this would trigger the voice assistant
        # For now, return a success message
        return jsonify({
            'success': True,
            'message': 'Listening started. Say "Jarvis" followed by your command.'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/mute', methods=['POST'])
def mute():
    """Toggle voice output"""
    global voice_enabled
    data = request.json
    voice_enabled = not data.get('muted', False)
    
    return jsonify({
        'success': True,
        'voice_enabled': voice_enabled
    })

@app.route('/api/command', methods=['POST'])
def process_command():
    """Process a text command (for testing without voice)"""
    data = request.json
    command = data.get('command', '')
    
    # Simple command processing
    response = f"Received command: {command}"
    
    if 'time' in command.lower():
        from datetime import datetime
        response = f"The current time is {datetime.now().strftime('%I:%M %p')}"
    elif 'hello' in command.lower() or 'hi' in command.lower():
        response = "Hello! I am Jarvis, your AI assistant."
    elif 'joke' in command.lower():
        response = "Why do programmers prefer dark mode? Because light attracts bugs!"
    
    return jsonify({
        'success': True,
        'response': response
    })

if __name__ == '__main__':
    print("=" * 50)
    print("🤖 JARVIS Web Interface Starting...")
    print("=" * 50)
    print("\n📱 Open your browser to: http://localhost:5000")
    print("🌐 Or share with friends: http://YOUR_IP:5000")
    print("\n💡 To find your IP address, run: ipconfig")
    print("\n⚠️  Note: Voice features require running voice_assistant.py separately")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
