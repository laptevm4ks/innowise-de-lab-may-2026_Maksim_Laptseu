import pandas as pd
from sqlalchemy import create_engine, text

tables = ["countries", "cities", "categories", "products", "shops", "employees", "customers", "sales"]

try:
    engine = create_engine('sqlite:///bronze_data.db', echo=False)
    
    for table_name in tables:
        file_path = f"{table_name}.csv"
        df = pd.read_csv(file_path, sep=';', low_memory=False, engine='c')
        
        table_name = "bronze_"+table_name
        df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        print(f"Таблица '{table_name}' успешно загружена в базу.")

except FileNotFoundError as e:
    print(f"Ошибка: Не найден файл — {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
