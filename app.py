from flask import Flask, request
import os
import requests

app = Flask(__name__)

LINE_TOKEN = os.getenv("LINE_TOKEN")
TARGET_USER = os.getenv("TARGET_USER")


@app.route("/")
def home():
    return "FB Notify is running!"


@app.route("/callback", methods=["POST"])
def callback():
    data = request.json

    message = f"📩 Facebook Webhook\n\n{data}"

    requests.post(
        "https://api.line.me/v2/bot/message/push",
        headers={
            "Authorization": f"Bearer {LINE_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "to": TARGET_USER,
            "messages": [
                {
                    "type": "text",
                    "text": message[:4900]
                }
            ]
        }
    )

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
