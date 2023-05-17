# coding:utf-8


import json
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def index():
    return "HomePage"


@app.route("/hello_rec", methods=["POST"])
def hello_recommendation():
    try:
        if request.method == "POST":
            rec_json = request.get_data()
            rec_obj = json.loads(rec_json)
            user_id = rec_obj["user_id"]
            return jsonify({"code": 0, "msg": "请求成功", "data": "Hello, %s" % user_id})
    except:
        return json({"code": 2000, "msg": "error"})
    

@app.route("/hello_multiply", methods=["GET", "POST"])
def hello_multiply():
    try:
        if request.method == "POST":
            rec_json = request.get_data()
            rec_obj = json.loads(rec_json)
            # 乘数
            m = rec_obj["m"]
            # 被乘数
            n = rec_obj["n"]
            return jsonify({"code": 0, "msg": "请求成功", "data": m * n})
        
        if request.method == "GET":
            m = request.args.get("m")
            n = request.args.get("n")
            return f"{m} * {n} = {int(m) * int(n)}"
    except:
        return json({"code": 2000, "msg": "error"})


if __name__ == "__main__":
    app.run(debug=True)