daily_logs = [
    [500, 0, 1200],       # Касса 1 (Нормальная)
    [300, -999, 800],     # Касса 2 (Сломалась посередине, 800 не должно посчитаться)
    [1500, 200]           # Касса 3 (Нормальная)
]

total_revenue = 0

for i, cassa in enumerate(daily_logs):
    print(f'--- Обработка Кассы №{i+1} ---')

    for transaction in cassa:
        if transaction == -999:
            print("Аварийная остановка кассы!")
            break
        elif transaction == 0:
            print("Пропуск сбоя")
            continue
        else:
            total_revenue += transaction
            print(f'Добавлено {transaction}')
else:
    print(f'Итоговая выручка магазина: {total_revenue}')