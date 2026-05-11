product_name = "Морковь мытая"
price = 2.5
stock_quantity = 150
is_local_farm = True
supplier = None

has_coupon = True
has_card = False
total = 10

is_hit = price < 3 and is_local_farm
has_supplier = supplier is not None
can_show_in_app = (supplier is not None) and stock_quantity > 0
needs_restock = stock_quantity <= 20 or is_hit
is_blocked = not is_local_farm

discount_without_brackets = has_coupon or has_card and total > 50
discount_with_brackets = (has_coupon or has_card) and total > 50

print('Является ли товар хитом?', is_hit)
print('Поставщик указан?', has_supplier)
print('Показывать в приложении?', can_show_in_app)
print('Нужно пополнение?', needs_restock)
print('Товар заблокирован для акции?', is_blocked)

price += 1
stock_quantity *= 2
boxes = stock_quantity
boxes //= 10
is_hit = price < 3 and is_local_farm
needs_restock = stock_quantity <= 20 or is_hit


print('Скидка без скобок:', discount_without_brackets)
print('Скидка со скобками:', discount_with_brackets)

print('Цена после изменения:', price)
print('Остаток после изменения:', stock_quantity)
print('Полных коробок по 10 кг:', boxes)

print('Является ли товар хитом (после изменений)?', is_hit)
print('Нужно пополнение (после изменений)?', needs_restock)
