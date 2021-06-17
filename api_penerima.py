from flask import request, Flask, jsonify
import json
from sqlib import input_suhu_kelembapan, input_cahaya, input_hujan, get_cahaya, get_hujan, get_suhu_kelembapan

app = Flask(__name__)


@app.route('/ida/input/node1/<suhu>/<kelembapan>', methods=['POST'])
def input_node1(suhu, kelembapan):
    input_suhu_kelembapan(suhu, kelembapan)
    result = {"message": "Input success"}
    resp = jsonify(result)
    return resp, 200


@app.route('/ida/input/node2/<hujan>', methods=['POST'])
def input_node2(hujan):
    input_hujan(hujan)
    result = {"message": "Input success"}
    resp = jsonify(result)
    return resp, 200


@app.route('/ida/input/node3/<cahaya>', methods=['POST'])
def input_node3(cahaya):
    input_cahaya(cahaya)
    result = {"message": "Input success"}
    resp = jsonify(result)
    return resp, 200


@app.route('/ida/welcome', methods=['GET'])
def welcome():
    result = {"message": "welcome"}
    resp = jsonify(result)
    return resp, 200


@app.route('/ida/get/node1', methods=['GET'])
def get_node1():
    result = get_suhu_kelembapan()
    return result, 200


@app.route('/ida/get/node2', methods=['GET'])
def get_node2():
    result = get_hujan()
    return result, 200


@app.route('/ida/get/node3', methods=['GET'])
def get_node3():
    result = get_cahaya()
    return result, 200


if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=7001)
    app.run(port=7001, debug=True)
