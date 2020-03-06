from Utils.Bachmann_Brand_Purchase_Count import Bachmann_Brand_Purchase_Count
from Utils.Costly_Product import Costly_Product
from Utils.ReviewColor import ReviewColor
from Utils.costant import bachmann_count, id_cost, indivisual_count, selling_product, review_color
from Utils.MaleFemaleCount import MaleFemaleCount
from Utils.ProductRating3 import ProductRating3
from Utils.Selling_Product import Selling_Product


def test_Bachmann_Brand_Purchase_Count():
    Result = Bachmann_Brand_Purchase_Count.Bachmann_Brand_Purchase_Count()
    assert Result == bachmann_count


def test_Costly_Product():
    Result = Costly_Product.Costly_Product()
    assert Result == id_cost


def test_ProductRating3():
    Result = ProductRating3.ProductRating3()
    assert Result == Result


def test_Selling_Product():
    Result = Selling_Product.Selling_Product()
    assert Result == selling_product


def test_MaleFemaleCount():
    Result = MaleFemaleCount.MaleFemaleCount()
    assert Result == indivisual_count


def test_ReviewColor():
    Result = ReviewColor.Review_Color()
    assert Result == review_color
