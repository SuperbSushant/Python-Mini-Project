from Utils.Bachmann_Brand_Purchase_Count import Bachmann_Brand_Purchase_Count
from Utils.Costly_Product import Costly_Product
from Utils.MaleFemaleCount import MaleFemaleCount
from Utils.ProductRating3 import ProductRating3
from Utils.Selling_Product import Selling_Product
from Utils.ReviewColor import ReviewColor

class main:
    @staticmethod
    def getResult():
        return {
            "task1": Bachmann_Brand_Purchase_Count().Bachmann_Brand_Purchase_Count(),
            "task2": Costly_Product().Costly_Product(),
            "task3": ProductRating3().ProductRating3(),
            "task4": Selling_Product().Selling_Product(),
            "task5": MaleFemaleCount().MaleFemaleCount(),
            "task7": ReviewColor().Review_Color()

        }


obj_main = main()

print(obj_main.getResult())
