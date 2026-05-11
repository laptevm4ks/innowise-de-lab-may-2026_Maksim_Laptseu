product = " фермерский ТВОРОГ " 
price = 4.567 
qty = 3 
csv_row = "milk,bread,cheese" 
review = "Это лучший ТВОРОГ в городе!" 
file_path = r"C:\EcoMarket\data\2025\january\sales.csv"

clean_product = product.strip().title()
total = price * qty

print(f'Чек "EcoMarket"\nТовар: {clean_product}\nКол-во: {qty}\nИтого: {total} руб.')

csv_row_split = csv_row.split(',')
csv_row = ' | '.join(csv_row_split)
print(csv_row)

if "творог" in review.lower():
    print('Отзыв относится к категории: Dairy')

# file_path уже идет как r строка. Она сипользуется для того, чтобы игнорировать экранирование символов и спецсимволы
print(file_path)
