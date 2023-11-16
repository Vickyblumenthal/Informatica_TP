import csv
from clase_ropa import Ropa


def load_books():
    ropa = []
    with open('Ropa.csv', 'r') as ropa_file:
        rows = csv.DictReader(ropa_file)

        for row in rows:
            ropa.append(
                Ropa(
                    row['id'],
                    row['producto'],
                    row['precio'],
                    row['stock'],
                    row['material'],
                    row['color'],
                    row['tela']
                )
            )

        return ropa


def create_books(ropa_add):
    with open ('Ropa.csv', 'a', newline='') as output_file:
        header=ropa_add.keys()
        writer = csv.DictWriter(output_file, fieldnames=header)
        if output_file.tell()==0:
            writer.writerheader()
        writer.writerow(ropa_add)