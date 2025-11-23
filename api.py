from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # libera o acesso do front

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def gerar_resposta(prompt):
    print("Enviando para o Ollama:", prompt)
    print("Chamando IA...")
    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt},
        stream=True
    )
    print("Resposta da IA chegou")

    resposta_final = ""

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            if "response" in data:
                resposta_final += data["response"]

    return resposta_final


@app.post("/chat")
def chat():
    dados = request.json
    mensagem = dados.get("mensagem", "")

    resposta = gerar_resposta(mensagem)
    return jsonify({"resposta": resposta})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
