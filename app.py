# app.py
from flask import Flask, render_template, request, jsonify
from agent import get_answer

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()
    answer = get_answer(user_message)
    return jsonify({"answer": answer})

if __name__ == "__main__":   # ✅ FIXED
    app.run(debug=True)
