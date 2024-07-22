from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Load your API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load corpus data from JSON file
with open('sample_question_answers.json', 'r') as f:
    corpus = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response_text = get_response_from_corpus(user_message)
    return jsonify({"response": response_text})

def get_response_from_corpus(message):
    # Implement logic to match user query with corpus
    for item in corpus:
        if item['question'].lower() in message.lower():
            return item['answer']
    return "Please contact our business directly for more information."

if __name__ == '__main__':
    app.run(debug=True)
