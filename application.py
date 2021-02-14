from flask import Flask, render_template, request, jsonify

from vk import make_call

app = Flask(__name__)

@app.route("/calendar")
def calendar():
    return render_template("birthday.html")

@app.route("/api/vk", methods=["POST"])
def vk():
    id = request.form["id"]
    data = make_call(id)
    if data:
        return jsonify({
            "success": True,
            "data": data
        })
    else:
        return jsonify({
            "success": False,
            "data": "Nothing was found"
        })