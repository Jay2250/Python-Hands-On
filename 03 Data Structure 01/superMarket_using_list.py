item = []
price = []
quantity = []
while True:
  item.append(input("Enter the item "))
  price.append(int(input("Enter the price ")))
  quantity.append(int(input("Enter the quantity ")))
  choice = input(" do you want to add more items type 'yes/no'")
  if choice != 'yes':
    break
store_data = {item[i]:[{"quantity":quantity[i]},{"price":price[i]}] for i in range(0,len(item))}
print(store_data)
updateItem = input("Enter item to be updated.. ")
updatePrice = int(input("Enter new price "))
updateQuantity = int(input("Enter new quantity "))
store_data[updateItem]=[{"quantity":updateQuantity},{"price":updatePrice}]
print(store_data)
value = 0
for i in store_data.values():
  value += i[0]["quantity"] * i[1]["price"]    #[{'quantity': 10}, {'price': 500}]    here quantity is a key of the dict inside the list
print("Total value of items is : ",value)