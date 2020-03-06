import csv


class ReviewColor:
    @staticmethod
    def Review_Color():
        color_list = []
        review_list = []
        temp_color = []
        with open('/home/hasher/Python_Project/python-mini-project/Clothing.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                color_list.append(line[3])
                review_list.append(line[8])
            for index, key in enumerate(review_list):
                if key == 'Bad Quality':
                    temp_color.append(color_list[index])
            count = 0
            color = ''
            for item in set(temp_color):
                count_new = temp_color.count(item)
                if count_new > count:
                    count = count_new
                    color = item
            return color

