from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calcular-impuestos', methods=['POST'])
def calcular_impuestos():
    try:
        data = request.get_json()

        if not data or "valorBase" not in data:
            return jsonify({"error": "Falta el campo 'valorBase'"}), 400

        valor_base = float(data.get("valorBase"))
        medio_pago = data.get("medioPago", "N/A")

        iva = round(valor_base * 0.19, 2)
        retencion = round(valor_base * 0.12, 2)

        return jsonify({
            "iva": iva,
            "retencion": retencion
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=8001, debug=True)
