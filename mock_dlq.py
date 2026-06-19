from flask import Flask, request, jsonify

app = Flask(__name__)
stored_messages = []

@app.route('/dlq/messages', methods=['POST'])
def receive_dlq():
    data = request.json
    print(f"📥 Message reçu dans la DLQ : {data}")
    stored_messages.append(data)
    return jsonify({"status": "stored"}), 201

@app.route('/dlq/messages', methods=['GET'])
def get_dlq():
    return jsonify(stored_messages)

if __name__ == '__main__':
    app.run(port=3000)