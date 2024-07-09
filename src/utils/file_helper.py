from json import loads, dumps


class FileHelper():
    data_file: str

    def __init__(self, data_file):
        self.data_file = data_file

    def read_products_file(self):
        with open(self.data_file, "r") as file:
            products = list(loads(file.read()))

        return products

    def write_product_to_file(self, product: dict):
        products = read_products_file()

        product["id"] = len(products) + 1

        products.append(product)
        with open(self.data_file, mode="w")as file:
            file.write(dumps(products))

    def update_product_to_file(self, id: int, update_product: dict):
        products = read_products_file()
        for product in products:
            if product.get("id") == id:
                for key in update_product.keys():
                    if update_product[key]:
                        product[key] = update_product[key]
        with open(self.data_file, mode="w")as file:
            file.write(dumps(products))

    def delete_product_to_file(self, id: int):
        products = read_products_file()
        products = list(filter(lambda obj: obj.get("id") != id, products))
        with open(self.data_file, mode="w")as file:
            file.write(dumps(products))
