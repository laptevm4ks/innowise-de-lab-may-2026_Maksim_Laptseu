import json 
api_response_json = """ 
{ 
	"store": "StoreHub", 
	"orders": [ 
		{"id": 1, "total": 50}, 
		{"id": 2, "total": 200}, 
		{"id": 3, "total": 150} 
		]
 } 
"""

api_response = json.loads(api_response_json)

orders_list = api_response["orders"]
high_value_orders = [order for order in orders_list if order["total"] > 100]

api_response["high_value_orders"] = high_value_orders

api_response_json = json.dumps(api_response)
print(api_response_json)