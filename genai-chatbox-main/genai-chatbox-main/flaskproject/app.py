import os
import json
import base64
import logging
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the desired log level

app = Flask(__name__)

os.environ['GOOGLE_API_KEY'] = "AIzaSyDnhDLrV74ffbfHx7fEto9Mf_SEquohqao"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model1 = genai.GenerativeModel('gemini-pro')
chat_model = genai.GenerativeModel('gemini-pro')

# Initialize chat history
chat = chat_model.start_chat(history=[])

@app.errorhandler(Exception)
def handle_error(error):
    app.logger.error('An error occurred: %s', error)
    return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/')
def chat_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def chat_with_ai():
    try:
        message = request.form.get('message')
        if not message:
            return jsonify({'error': 'Message is required'}), 400

        # Send message to the Generative AI model
        response = chat.send_message(message)

        # Return the response
        return jsonify({'response': response.text})
    except Exception as e:
        app.logger.error('An error occurred while processing chat request: %s', e)
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/history', methods=['GET'])
def get_chat_history():
    try:
        # Return the chat history
        return jsonify({'history': chat.history})
    except Exception as e:
        app.logger.error('An error occurred while getting chat history: %s', e)
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
