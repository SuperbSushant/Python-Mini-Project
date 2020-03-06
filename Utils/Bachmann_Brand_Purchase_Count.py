import csv


class Bachmann_Brand_Purchase_Count:
    @staticmethod
    def Bachmann_Brand_Purchase_Count():
        with open('/home/hasher/Python_Project/python-mini-project/Clothing.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            lineInc = 0
            for line in csv_reader:
                if line[2] == "Bachmann":
                    lineInc = lineInc + 1
            return lineInc
