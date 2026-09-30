from flask import Flask, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAAaa60CXIFUBSoGDDgmcHTilpboI0RFuYPRGghWaaRYNnslnyWOEU8OXqZAEM0K2cEhvhF2NDVIRqtmFKfWn44ys9dwmtX6Aro9TZCmeKgQXJVzJGy9BRhY9gzZCxDSJCXOZAnPjgCBP7eZB4ynun80YxTkJt2ZAIP1jc8RIbqE6U0uSZCUbbLWQw9nquAEzkuOL"
PHONE_NUMBER_ID = "1371214036073162"
VERIFY_TOKEN = "kabeer123"

@app.route("/")
def home():
    return "Kabeer Bot is Live!"

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    try:
        entry = data['entry'][0]['changes'][0]['value']
        if 'messages' in entry:
            message = entry['messages'][0]
            from_number = message['from']
            msg_body = message['text']['body']

            url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
            headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
            payload = {
                "messaging_product": "whatsapp",
                "to": from_number,
                "text": {"body": f"Mil gaya Kabeer! Tune bheja: {msg_body} - Bot LIVE hai 🔥"}
            }
            requests.post(url, headers=headers, json=payload)
    except Exception as e:
        print(e)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
