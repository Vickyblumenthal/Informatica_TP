from flask import jsonify

from db_ropa import get_db
from clase_ropa import Ropa
import sqlite3

ROPA_DB_FILE = "ropa.db"
def get_db():
    conn = sqlite3.connect(ROPA_DB_FILE)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS productos(
                ID INTEGER PRIMARY KEY,
                producto TEXT NOT NULL,
                precio INTEGER NOT NULL,
                stock INTEGER NOT NULL,
                material TEXT NOT NULL,
                color TEXT NOT NULL,
                tela TEXT NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)


def insert_ropa(ID, producto, precio, stock, material, color, tela):
    db = get_db()
    cursor = db.cursor()
    statement = ("INSERT INTO productos (ID, producto, precio, stock, material, color, tela) "
                 "VALUES (?, ?, ?, ?, ?, ?, ?)")
    cursor.execute(statement, [ID, producto, precio, stock, material, color, tela])
    db.commit()
    return True

def update_ropa(id, producto, precio, stock, material, color, tela):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE productos SET id = ?, producto = ?, precio = ?, stock = ?, material = ?, color = ?, tela = ? \
    WHERE id = ?"
    cursor.execute(statement, [id, producto, precio, stock, material, color, tela, id])
    db.commit()
    return True


def delete_ropa(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM productos WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, producto, precio, stock, material, color, tela FROM productos WHERE id = ?"
    cursor.execute(statement, [id])
    single_ropa = cursor.fetchone()

    if single_ropa is None:
        return None

    id = single_ropa[0]
    producto = single_ropa[1]
    precio = single_ropa[2]
    stock = single_ropa[3]
    material = single_ropa[4]
    color = single_ropa[5]
    tela = single_ropa[6]
    ropa = Ropa(id, producto, precio, stock, material, color, tela)
    return ropa.serialize_details()


def get_ropas():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT ID, producto, precio, stock, material, color, tela FROM productos"
    cursor.execute(query)
    ropa_list = cursor.fetchall()
    list_of_ropas=[]
    for ropa in ropa_list:
        ID = ropa[0]
        producto = ropa[1]
        precio = ropa[2]
        stock = ropa[3]
        material = ropa[4]
        color = ropa[5]
        tela = ropa[6]
        ropa_to_add = Ropa(ID, producto, precio, stock, material, color, tela)
        list_of_ropas.append(ropa_to_add)
    return list_of_ropas


def menu():
    print('******************Menu******************')
    print()
    print('ingrese 0 para cargar desde archivo de texto')
    print('ingrese 1 para agregar un producto a la base de datos')
    print ('ingrese 2 para eliminar un producto de la base de datos')
    print ('ingrese 3 para buscar un producto por su id')
    print('ingrese 4 para listar todos los productos')
    print ('ingrese 5 para salir del menu')

    create_tables()
    flag = 1
    while flag:
        menu()

        opcion = int(input())
        if opcion == 0:
            load_books()

        elif opcion == 1:
            id = int(input('ingrese el id del producto: '))
            producto = input('ingrese el nombre del producto:')
            precio = input('ingrese el precio del producto: ')
            stock = float(input('ingrese la cantidad de stock del producto: '))
            material = int(input('ingrese el material del producto: '))
            color = input('ingrese el color del producto: ')
            tela = int(input('ingrese la tela del prdocuto: '))
            result = insert_ropa(id, producto, precio, stock, material, color, tela)
            if result == True:
                print('El producto ha sido ingresado correctamente')
                print()
                print()
            else:
                print('Error')
                print()

        elif opcion == 2:
            id = int(input('ingrese el id del producto que desea eliminar'))
            result = delete_ropa(id)
            if result == True:
                print('El producto ha sido eliminado')
                print()
                print()
            else:
                print('Error')
                print()

        elif opcion == 3:
            id = int(input('ingrese el id del proudcto que desea buscar'))
            result = get_by_id(id)  # devuelve una tupla con el registro
            if id not in ROPA_DB_FILE:
                print(result)
                print()
                print()
            else:
                print('Error')
                print()


        elif opcion == 4:
            result = get_ropas()  # devuelve una lista de tuplas donde cada tupla es un registro
            print(result)
            print()
            print()

        elif opcion == 5:
            print()
            print('saliendo')
            print()
            flag = False

    print('terminado')
    print('****************************************************')