import csv


class Costly_Product:
    @staticmethod
    def Costly_Product():
        priceList = []
        product_id = []
        with open('/home/hasher/Python_Project/python-mini-project/Clothing.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                product_id.append(int(line[0]))
                priceList.append(int(line[6]))
            return product_id[priceList.index(max(priceList))]
