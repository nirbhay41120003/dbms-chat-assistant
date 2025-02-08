import os
from flask import Flask, render_template, request, jsonify
from chat_assistant import DatabaseChatAssistant

app = Flask(__name__)
assistant = DatabaseChatAssistant()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def process_query():
    user_query = request.json.get('query', '')
    if not user_query:
        return jsonify({'error': 'No query provided'})
    
    response = assistant.process_query(user_query)
    return jsonify({'response': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
