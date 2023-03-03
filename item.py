import csv


class Item:
    instances = []
    num_of_item = 0
    pay_rate = 0.85

    def __init__(self, product: str, quanity: int, price: int):
        self.__product = product
        self.quanity = quanity
        self.price = price
        self.instances.append(self)
        Item.num_of_item += 1

    def calculate_total_price(self):
        return self.quanity * self.price

    @property
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        results = []
        with open('items.csv', encoding='windows - 1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                __product = row['name']
                price = cls.is_integer(int(row['price']))
                quanity = cls.is_integer(int(row['quantity']))
                results.append(cls(__product, quanity, price))

        return results

    @staticmethod
    def is_integer(number):
        if number % 1 == 0:
            return True
        else:
            return False

    @property
    def long_name(self):
        return self.__product

    @long_name.setter
    def long_name(self, name):

        try:
            if len(name) > 10:
                raise Exception('name must be less than 10')
        except Exception:
            print('Длина наименования товара превышает 10 символов')
        self.__product = name
