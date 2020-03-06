import csv


class Selling_Product:
    @staticmethod
    def Selling_Product():
        product_list = []
        quantity_list = []
        product_dict = {}
        with open('/home/hasher/Python_Project/python-mini-project/Clothing.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                product_list.append(line[1])
                quantity_list.append(line[4])
            product_set = set(product_list) #Creating set of products
            for key in product_set:
                product_dict[key] = 0
            for index, item in enumerate(product_list):
                product_dict[item] = int(product_dict[item]) + int(quantity_list[index])
            product_list = max(product_dict, key=product_dict.get)
            return product_list

