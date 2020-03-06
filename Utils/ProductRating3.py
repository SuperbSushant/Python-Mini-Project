import csv


class ProductRating3:
    @staticmethod
    def ProductRating3():
        product_list = []
        rating_list = []
        temp_product = []
        final_list = []
        with open('/home/hasher/Python_Project/python-mini-project/Clothing.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                product_list.append(line[1])
                rating_list.append(line[7])
            for index, key in enumerate(rating_list):
                if int(key) == 3:
                    temp_product.append(product_list[index])
            for item in set(temp_product):
                count = temp_product.count(item)
                if count > 1:
                    final_list.append(item)
            return final_list
