import subprocess
import socket
from flask import Flask, request, jsonify
from llm_axe import OnlineAgent, OllamaChat

def find_available_port(starting_port=5000):
    port = starting_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
        port += 1

def start_flask_server():
    app = Flask(__name__)
    model = "deepseek-r1:1.5b"
    llm = OllamaChat(model=model)
    online_agent = OnlineAgent(llm)
    
    @app.route('/generate', methods=['POST'])
    def generate():
        data = request.get_json()
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400
        
        response = online_agent.search(prompt)
        return jsonify({"response": response})
    
    port = find_available_port()
    server_address = f"http://127.0.0.1:{port}"
    print(f"Starting Flask server...")
    print(f"Server running at {server_address}")
    print(f"Send POST requests to {server_address}/generate")
    
    app.run(host='0.0.0.0', port=port, debug=False)

def main():
    start_flask_server()

if __name__ == "__main__":
    main()
