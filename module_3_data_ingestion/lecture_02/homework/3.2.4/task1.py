raw_log = "ORDER-2025-01-15|FRT-APPLE-PL|+111 (23) 456-78-90| мИНсК "

order_id, product_code, raw_phone, raw_city = raw_log.split("|")

print(f'Позиция первого дефиса в коде товара: {product_code.find('-')}')

if product_code.startswith('FRT'):
    print("Код товара начинается с 'FRT'")
else:
    print("Код товара НЕ начинается с 'FRT'")

clean_phone = ''
for char in raw_phone:
    if char.isdigit():
        clean_phone += char
print(f'Длина номера телефона: {len(clean_phone)}')

print(f'Заказ: {order_id}')

print(f'Категория: {product_code[:3]} | Регион: {product_code[-2:]}')

print(f'Телефон: {clean_phone}')

print(f'Город: {raw_city.strip().title()}')