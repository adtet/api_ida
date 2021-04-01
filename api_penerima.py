from flask import request, Flask, jsonify
import json
from sqlib import input_suhu_kelembapan, input_cahaya, input_hujan, get_cahaya, get_hujan, get_suhu_kelembapan

app = Flask(__name__)


@app.route('/input/node1', methods=['POST'])
def input_node1():
    json_data = request.json
    if json_data == None:
        result = {"message": "process failed"}
        resp = jsonify(result)
        return resp, 400
    else:
        if 'suhu' not in json_data or 'kelembapan' not in json_data:
            result = {"message": "error request"}
            resp = jsonify(result)
            return resp, 401
        else:
            suhu = json_data['suhu']
            kelembapan = json_data['kelembapan']
            input_suhu_kelembapan(suhu, kelembapan)
            result = {"message": "Input success"}
            resp = jsonify(result)
            return resp, 200


@app.route('/input/node2', methods=['POST'])
def input_node2():
    json_data = request.json
    if json_data == None:
        result = {"message": "process failed"}
        resp = jsonify(result)
        return resp, 400
    else:
        if 'hujan' not in json_data:
            result = {"message": "error request"}
            resp = jsonify(result)
            return resp, 401
        else:
            hujan = json_data['hujan']
            input_hujan(hujan)
            result = {"message": "Input success"}
            resp = jsonify(result)
            return resp, 200


@app.route('/input/node3', methods=['POST'])
def input_node3():
    json_data = request.json
    if json_data == None:
        result = {"message": "process failed"}
        resp = jsonify(result)
        return resp, 400
    else:
        if 'cahaya' not in json_data:
            result = {"message": "error request"}
            resp = jsonify(result)
            return resp, 401
        else:
            cahaya = json_data['cahaya']
            input_cahaya(cahaya)
            result = {"message": "Input success"}
            resp = jsonify(result)
            return resp, 200


@app.route('/get/node1', methods=['GET'])
def get_node1():
    result = get_suhu_kelembapan()
    return result, 200


@app.route('/get/node2', methods=['GET'])
def get_node2():
    result = get_hujan()
    return result, 200


@app.route('/get/node3', methods=['GET'])
def get_node3():
    result = get_cahaya()
    return result, 200


if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=7001)
    app.run(port=7001, debug=True)
