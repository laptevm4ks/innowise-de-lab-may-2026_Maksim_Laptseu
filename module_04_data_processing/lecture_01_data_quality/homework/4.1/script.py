import pandas as pd
from sqlalchemy import create_engine
import datetime

def validate_and_fix_date(date_str):
    if pd.isna(date_str) or str(date_str).strip() == '':
        return datetime.date(1900, 1, 1)
    
    date_str = str(date_str).replace('/', '-')
    
    formats = ['%Y-%m-%d', '%d-%m-%Y', '%m-%d-%Y']
    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt).date()
        except (ValueError, TypeError):
            continue
            
    return datetime.date(1900, 1, 1)

tables = ["countries", "cities", "categories", "products", "shops", "employees", "customers", "sales"]

try:
    engine = create_engine("postgresql+psycopg2://admin:admin123@localhost:5433/postgre", echo=False)
    
    for table_name in tables:
        file_path = f"{table_name}.csv"
        df = pd.read_csv(file_path, sep=';', low_memory=False, engine='c')

        if table_name == "employees":
            df['birth_date'] = df['birth_date'].apply(validate_and_fix_date)
            df['hire_date'] = df['hire_date'].apply(validate_and_fix_date)

        elif table_name == "products":
            df['resistant'] = df['resistant'].map({'1': True, '0': False, 1: True, 0: False})
            df['is_allergic'] = df['is_allergic'].map({'1': True, '0': False, 1: True, 0: False})
            df['price'] = pd.to_numeric(df['price']).round(2)

        elif table_name == "sales":
            df = df.dropna(subset=['sales_timestamp'])
            df['sales_timestamp'] = pd.to_datetime(df['sales_timestamp'], errors='coerce')
            df = df.dropna(subset=['sales_timestamp'])
            
            df['discount'] = pd.to_numeric(df['discount']).round(2)
            df['total_price'] = pd.to_numeric(df['total_price']).round(2)
            

            if 'city_id' not in df.columns: df['city_id'] = None
            if 'shop_id' not in df.columns: df['shop_id'] = None
        
        target_table = "silver_" + table_name
        df.to_sql(
            name=target_table, 
            con=engine, 
            schema='silver', 
            if_exists='append', 
            index=False
        )
        print(f"Таблица '{target_table}' успешно обработана и загружена.")

except FileNotFoundError as e:
    print(f"Ошибка: Не найден файл — {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")