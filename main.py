from item import Item

item1 = Item("Смартфон", 20, 10000)
item2 = Item("Ноутбук", 5, 20000)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

Item.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount
print(int(item1.price))
print(item2.price)

print(Item.instances)

Item.instantiate_from_csv()  # создание объектов из данных файла

print(len(Item.instantiate_from_csv()))
item1 = Item.instantiate_from_csv()[0]

print(item1._Item__product)

item = Item('Телефон', 10000, 5)

item.long_name = 'Смартфон'
print(item.long_name)

print(item._Item__product)
item.long_name = 'СуперСмартфон'
print(Item.is_integer(5))
print(Item.is_integer(5.0))
print(Item.is_integer(5.5))
