from flask import Flask, request, jsonify
from order import process_order

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    components = data.get('components', [])
    
    if not components:
        return jsonify({"error": "No components provided"}), 400

    parts, total = process_order(components)
    
    response_data = {
        "order_id": "123",
        "total": round(total, 2),
        "parts": parts
    }
    
    return jsonify(response_data), 201

if __name__ == '__main__':
    app.run(debug=True)
