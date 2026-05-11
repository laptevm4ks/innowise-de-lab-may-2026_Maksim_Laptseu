usd_prices = { 
"Banana": 1.2, 
"Mango": 2.5, 
"Avocado": 2.0 
}

eur_prices = {fruit: price * 0.9 for fruit, price in usd_prices.items()}

print(eur_prices)