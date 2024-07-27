from flask import Flask, request, jsonify, send_from_directory
import datetime
import webbrowser
import logging
import subprocess  # Import subprocess for executing system commands

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/command', methods=['POST'])
def command():
    data = request.get_json()
    command = data.get('command', '').lower()
    app.logger.debug(f"Received command: {command}")  # Debug information
    
    response = "I didn't understand that command."
    
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}"
    elif 'open google' in command:
        webbrowser.open('https://www.google.com')
        response = 'Opening Google'
    elif 'open youtube' in command:
        webbrowser.open('https://www.youtube.com')
        response = 'Opening YouTube'
    elif 'open notepad' in command:
        try:
            subprocess.Popen('notepad.exe')  # Open Notepad
            response = 'Opening Notepad'
        except Exception as e:
            response = f"Failed to open Notepad: {str(e)}"
    elif 'stop' in command:
        response = 'Stopping the assistant. Goodbye!'
    
    app.logger.debug(f"Response: {response}")  # Debug information
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
