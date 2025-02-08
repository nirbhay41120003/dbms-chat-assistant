from flask import Flask, render_template, request, jsonify
from chat_assistant import DatabaseChatAssistant
import os

app = Flask(__name__)
assistant = DatabaseChatAssistant()

# Ensure the database exists
if not os.path.exists('company.db'):
    from setup_database import create_database
    create_database()

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
    app.run(debug=True)