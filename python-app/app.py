from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route("/parse")
def parse():
    data = request.args.get("data")
    return yaml.load(data)   # vulnerable (RCE)
