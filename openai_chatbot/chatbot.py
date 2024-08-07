import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv

#load environment variable from .env file
load_dotenv()

# Set up the OpenAI client
api_key = os.getenv("OPEN_API_KEY")
client = OpenAI(api_key=api_key)

app = Flask(__name__, static_folder="../static", template_folder="../templates")

# Store conversation state
conversation = [{"role": "system", "content": "You are a healthcare assistant. Provide accurate and helpful healthcare information and diagnoses based on user symptoms."}]

def is_healthcare_related(prompt):
    healthcare_keywords = [
        "symptom", "diagnosis", "health", "doctor", "medicine", "treatment",
        "medical", "illness", "disease", "pain", "fever", "injury", "infection",
        "therapy", "prescription", "clinic", "hospital", "nurse", "emergency",
        "surgery", "cough", "cold", "flu", "virus", "bacteria", "rash", "allergy",
        "headache", "migraine", "stomachache", "fracture", "burn", "wound"
    ]
    prompt_lower = prompt.lower()
    for keyword in healthcare_keywords:
        if keyword in prompt_lower:
            return True
    return False

def chat_gpt(prompt):
    global conversation
    if not is_healthcare_related(prompt):
        return "I'm here to provide healthcare assistance. Please ask a health-related question."

    conversation.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    reply = response.choices[0].message.content.strip()
    conversation.append({"role": "assistant", "content": reply})
    return reply

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    response = chat_gpt(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
