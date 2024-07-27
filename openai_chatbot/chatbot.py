from dotenv import load_dotenv
from flask import Flask, request, jsonify
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or "gpt-4" if you have access
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    if user_input:
        bot_response = get_openai_response(user_input)
        return jsonify({"response": bot_response})
    return jsonify({"error": "No message provided"}), 400

# def chat_with_gpt():
#     print("Chat with OpenAI. Type 'exit' to end the conversation.")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'exit':
#             print("Ending conversation.")
#             break
#         bot_response = get_openai_response(user_input)
#         print(f"Bot: {bot_response}")

if __name__ == "__main__":
    app.run(debug=True)
