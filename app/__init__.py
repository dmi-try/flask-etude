from flask import Flask, jsonify, request
import os
import math
from datetime import datetime as dt

app = Flask(__name__)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/ping_json")
def ping_json():
    return jsonify({'ping': 'pong'})


@app.route("/days_counter")
def days_counter():
    def ordinal(n):
        return "%d%s" % (n, "tsnrhtdd"[
            (math.floor(n / 10) % 10 != 1) * (n % 10 < 4) * n % 10::4
        ])
    start_date = request.args.get('since')
    title = request.args.get('title')
    total = int(request.args.get('needed'))
    delta = (dt.today() - dt.strptime(start_date, '%Y-%m-%d')).days + 1
    return """
Today is the {days} day of {title}. {left} to go. {percent}% complete.
    """.format(
        days=ordinal(delta), title=title, left=total - delta,
        percent="%.0f" % (100*delta/total)
    )


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
