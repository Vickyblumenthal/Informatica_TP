--
-- Archivo generado con SQLiteStudio v3.4.4 el Tue Nov 14 13:20:51 2023
--
-- Codificaci�n de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabla: productos
CREATE TABLE IF NOT EXISTS productos (ID INTEGER PRIMARY KEY, Producto TEXT NOT NULL, Precio REAL NOT NULL, Stock INTEGER NOT NULL, Material TEXT NOT NULL, Color TEXT NOT NULL, Tela TEXT NOT NULL);
INSERT INTO productos (ID, Producto, Precio, Stock, Material, Color, Tela) VALUES (123, 'Remera1', 1200.0, 100, 'Algodon', 'Negro', 'Cardado');
INSERT INTO productos (ID, Producto, Precio, Stock, Material, Color, Tela) VALUES (234, 'Remera2', 1200.0, 120, 'Poliester', 'Blanco', 'Semipeinado');
INSERT INTO productos (ID, Producto, Precio, Stock, Material, Color, Tela) VALUES (345, 'Remera3', 1500.0, 150, 'Nylon', 'Rojo', 'Peinado');
INSERT INTO productos (ID, Producto, Precio, Stock, Material, Color, Tela) VALUES (456, 'Pantalon1', 2000.0, 40, 'Algodon', 'Azul', 'Jean');
INSERT INTO productos (ID, Producto, Precio, Stock, Material, Color, Tela) VALUES (567, 'Pantalon3', 2300.0, 60, 'Poliester', 'Beige', 'Lino');
INSERT INTO productos (ID, Producto, Precio, Stock, Material, Color, Tela) VALUES (678, 'Pantalon3', 2700.0, 80, 'Nylon', 'Gris', 'Sastrero');
INSERT INTO productos (ID, Producto, Precio, Stock, Material, Color, Tela) VALUES (789, 'Buzos1', 3000.0, 50, 'Algodon', 'Celeste', 'Frizada');
INSERT INTO productos (ID, Producto, Precio, Stock, Material, Color, Tela) VALUES (891, 'Buzos2', 3300.0, 70, 'Poliester', 'Rosa', 'Rustico');
INSERT INTO productos (ID, Producto, Precio, Stock, Material, Color, Tela) VALUES (910, 'Buzos3', 3800.0, 90, 'Nylon', 'Bordo', 'Lycra');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
