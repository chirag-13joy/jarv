from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'online',
        'voice_enabled': True
    })

@app.route('/api/speak', methods=['POST'])
def speak():
    # This would integrate with your voice_assistant.py
    # For now, returning a mock response
    return jsonify({
        'success': True,
        'message': 'Listening started'
    })

@app.route('/api/mute', methods=['POST'])
def mute():
    data = request.json
    muted = data.get('muted', False)
    
    # This would set the VOICE_ENABLED global in voice_assistant.py
    return jsonify({
        'success': True,
        'muted': muted
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
