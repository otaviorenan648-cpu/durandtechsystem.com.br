from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SITE = "https://www.durandtechsysten.com.br"
PIX = "00895672006"
JULIANA_ZAP = "https://wa.me/5548998290105?text=Oi%20Juliana!%20Maquininha%20Ton%20200,74%25"

@app.route("/")
def home():
    return jsonify({"status":"Durand Tech Bot Online com Juliana", "site": SITE, "pix": PIX})

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")
    return jsonify({"reply": f"Juliana recebeu: {msg}", "pix": PIX, "zap": JULIANA_ZAP})

# Linha obrigatória pro Vercel
app = app