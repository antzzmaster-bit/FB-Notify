from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "FB Notify is running!"

@app.route("/callback", methods=["POST"])
def callback():
    print(request.json)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
