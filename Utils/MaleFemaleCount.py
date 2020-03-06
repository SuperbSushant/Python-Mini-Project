import csv


class MaleFemaleCount:
    @staticmethod
    def MaleFemaleCount():
        size = []
        gender = []
        gender_count = []
        final_gender_list = {
            'male': 0,
            'female': 0
        }
        with open('/home/hasher/Python_Project/python-mini-project/Clothing.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for line in csv_reader:
                size.append(line[5])
                gender.append(line[13])
            for index, item in enumerate(size):
                if item == 'S':
                    gender_count.append(gender[index])
                final_gender_list['male'] = gender_count.count('Male')
                final_gender_list['female'] = gender_count.count('Female')
        return final_gender_list

