from flask import Flask, jsonify, request
from db_ropa import create_tables
import ropa_controller_poo


app = Flask(__name__)
DATABASE_NAME = "ropa.db"

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
    ID = ropa_details["ID"]
    producto = ropa_details["producto"]
    precio = ropa_details["precio"]
    stock = ropa_details["stock"]
    material = ropa_details["material"]
    color = ropa_details["color"]
    tela = ropa_details["tela"]
    result = ropa_controller_poo.insert_ropa(ID, producto, precio, stock, material, color, tela)
    if result:
        message = "El producto se creó correctamente."
    else:
        message = "Hubo un problema al intentar crear el producto."

    return jsonify({"message": message})


@app.route("/ropa/modify", methods=["PUT"])
def update_ropa():
    ropa_details = request.get_json()
    ID = ropa_details["ID"]
    producto = ropa_details["producto"]
    precio = ropa_details["precio"]
    stock = ropa_details["stock"]
    material = ropa_details["material"]
    color = ropa_details["color"]
    tela = ropa_details["tela"]
    result = ropa_controller_poo.update_ropa(ID, producto, precio, stock, material, color, tela)
    return jsonify(result)

@app.route("/ropa/eliminate/<id>", methods=["DELETE"])
def delete_ropa(id):
    result = ropa_controller_poo.delete_ropa(id)
    return jsonify(result)


@app.route("/ropa/<id>", methods=["GET"])
def get_ropa_by_id(id):
    ropa = ropa_controller_poo.get_by_id(id)

    if ropa is None:
        return jsonify({"error": "Ropa no encontrada"}), 404

    return jsonify(ropa.serialize_details())

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=5001)
