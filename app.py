from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route("/")
def home():
    return "Protect my channel API is running."

@app.route("/check", methods=["POST"])
def check_message():
    data = request.get_json()
    msg = data.get("message", "").lower()

    spam_keywords = ["airdrop", "crypto", "giveaway", "investment", "money"]
    if any(word in msg for word in spam_keywords):
        return jsonify({"reply": "🚫 This message was detected as spam."})
    else:
        return jsonify({"reply": "✅ Thank you for your message. We'll respond shortly!"})

if __name__ == "__main__":
    app.run()
