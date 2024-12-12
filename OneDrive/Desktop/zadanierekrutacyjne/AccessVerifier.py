from flask import Flask, request, jsonify

app = Flask(__name__)


allowed_ips = {
    # https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-ip-address.html
    "34.242.64.82", "52.18.37.201", "54.77.75.62",      # Europe (Ireland)
    "3.9.97.205", "35.177.150.185", "35.177.200.225",   # Europe (London)
    "35.181.127.138", "35.181.145.22", "35.181.20.200",# Europe (Paris)
}

@app.route('/verify', methods=['POST'])
def verify():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    client_ip = x_forwarded_for.split(',')[0].strip() if x_forwarded_for else request.remote_addr
    print("Received request from IP:", client_ip)

    if client_ip in allowed_ips:
        return jsonify({"message": "Access granted"}), 200
    else:
        return jsonify({"message": "Access denied"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)