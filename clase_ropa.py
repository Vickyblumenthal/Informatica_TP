class Ropa:

    def __init__(self, id, producto, precio, stock, material, color, tela) -> None:
        self.id = id
        self.producto = producto
        self.precio = precio
        self.stock = stock
        self.material = material
        self.color = color
        self.tela = tela

    def serialize(self):
        return {
            'id': self.id,
            'producto': self.producto,
            'precio': self.precio,
            'stock': self.stock
        }

    def serialize_details(self):
        return {
            'id': self.id,
            'producto': self.producto,
            'precio': self.precio,
            'stock': self.stock,
            'material': self.material,
            'color': self.color,
            'tela': self.tela,
        }
