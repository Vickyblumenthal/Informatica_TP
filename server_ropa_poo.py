from flask import Flask, jsonify, request
from db_ropa import create_tables
import ropa_controller_poo


app = Flask(__name__)

@app.route('/ropa', methods=["GET"])
def get_ropa():
    ropas = ropa_controller_poo.get_ropas()
    ropas_list = []
    for ropa in ropas:
        elem = ropa.serialize()
        ropas_list.append(elem)
    return jsonify(ropas_list)

@app.route("/ropa/create", methods=["POST"])
def insert_ropa():
    ropa_details = request.get_json()
    id = ropa_details["id"]
    producto = ropa_details["producto"]
    precio = ropa_details["precio"]
    stock = ropa_details["stock"]
    material = ropa_details["material"]
    color = ropa_details["color"]
    tela = ropa_details["tela"]
    result = ropa_controller_poo.insert_ropa(id, producto, precio, stock, material, color, tela)
    return jsonify(result)

@app.route("/ropa/modify", methods=["PUT"])
def update_ropa():
    ropa_details = request.get_json()
    id = ropa_details["id"]
    producto = ropa_details["producto"]
    precio = ropa_details["precio"]
    stock = ropa_details["stock"]
    material = ropa_details["material"]
    color = ropa_details["color"]
    tela = ropa_details["tela"]
    result = ropa_controller_poo.update_ropa(id, producto, precio, stock, material, color, tela)
    return jsonify(result)

@app.route("/ropa/eliminate/<id>", methods=["DELETE"])
def delete_ropa(id):
    result = ropa_controller_poo.delete_ropa(id)
    return jsonify(result)

@app.route("/ropa/<id>", methods=["GET"])
def get_ropa_by_id(id):
    ropa = ropa_controller_poo.get_by_id(id)
    return jsonify(ropa)

if __name__ == '__main__':
    app.run()
