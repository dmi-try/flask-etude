from flask import Flask, jsonify
import os
import pkg_resources

app = Flask(__name__)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/json_ping")
def json_ping():
    version = pkg_resources.get_distribution('app').version
    return jsonify({'ping': 'pong', 'version': version})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
