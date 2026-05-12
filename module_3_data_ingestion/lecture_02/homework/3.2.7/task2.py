branches = [
    {"city": "Minsk", "revenue": 15000},
    {"city": "Warsaw", "revenue": 32000},
    {"city": "London", "revenue": 12000}
]


def audit_logger(func):
    def wrapper(*args, **kwargs):
        print('[AUDIT] Запуск анализа....')
        result = func(*args, **kwargs)
        print('[AUDIT] Анализ завершен..')

        return result
    return wrapper

@audit_logger
def get_sorted_report(dict_list):
    sorted_dict_list = sorted(dict_list, key = lambda dict_list: dict_list["revenue"], reverse = True)
    return sorted_dict_list


sorted_dict_list = get_sorted_report(branches)

print('Топ фильмов:')
for i, filial in enumerate(sorted_dict_list):
    print(f'{i+1}. {filial["city"]}: {filial["revenue"]}')