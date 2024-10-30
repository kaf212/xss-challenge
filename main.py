from flask import Flask, jsonify, request
import re

app = Flask(__name__)

people = [
    {"name": "Alice Johnson", "age": 30},
    {"name": "Bob Smith", "age": 25},
    {"name": "Charlie Brown", "age": 35},
    {"name": "David Wilson", "age": 28},
]


@app.route("/xss", methods=["GET"])
def xss():
    """
    Dieser Endpoint ermöglicht reflektierte XSS-Attacken.
    TODO: Behebe die Sicherheitslücke im Code ohne die Funktionalität einzuschränken
          und teste deine Lösung mit main_test.py
    """
    query = request.args.get('q', '')
    regex = re.compile(query, re.IGNORECASE)
    results = [person for person in people if regex.search(person['name'])]

    return jsonify({"query": query, "results": results})


if __name__ == "__main__":
    app.run()
