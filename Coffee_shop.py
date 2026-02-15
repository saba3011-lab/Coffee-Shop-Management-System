# pro_coffee_shop_discount.py

menu = {
    "Coffee": [
        {"name": "Cappuccino", "price": 1200},
        {"name": "Latte", "price": 1300},
        {"name": "Espresso", "price": 1000},
        {"name": "Mocha", "price": 1400},
        {"name": "Americano", "price": 1100},
        {"name": "Macchiato", "price": 1250},
        {"name": "Flat White", "price": 1350},
        {"name": "Irish Coffee", "price": 1500},
        {"name": "Caramel Latte", "price": 1450},
        {"name": "Vanilla Cappuccino", "price": 1150},
    ],
    "Drinks": [
        {"name": "Hot Chocolate", "price": 1100},
        {"name": "Tea", "price": 1000},
        {"name": "Smoothie", "price": 1400},
        {"name": "Lemonade", "price": 1200},
        {"name": "Iced Coffee", "price": 1350},
        {"name": "Milkshake", "price": 1500},
        {"name": "Herbal Tea", "price": 1050},
        {"name": "Fruit Punch", "price": 1250},
        {"name": "Mango Lassi", "price": 1450},
        {"name": "Green Tea Latte", "price": 1150},
    ],
    "Snacks": [
        {"name": "Croissant", "price": 1000},
        {"name": "Muffin", "price": 1200},
        {"name": "Bagel", "price": 1100},
        {"name": "Sandwich", "price": 1300},
        {"name": "Donut", "price": 1050},
        {"name": "Brownie", "price": 1400},
        {"name": "Cookie", "price": 1150},
        {"name": "Cupcake", "price": 1250},
        {"name": "Scone", "price": 1350},
        {"name": "Panini", "price": 1500},
    ]
}

order = {}

def show_menu():
    print("\n--- Coffee Shop Menu ---")
    for cat, items in menu.items():
        print(f"\n== {cat} ==")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item['name']} - PKR {item['price']}")
    print("0. Finish Order")

def take_order():
    while True:
        show_menu()
        choice = input("Select category number or 0 to finish (format CatNum-ItemNum, e.g., 1-2): ")
        if choice == "0":
            break
        if '-' not in choice:
            print("Invalid format! Use CatNum-ItemNum like 1-2")
            continue
        cat_num_str, item_num_str = choice.split('-')
        if not (cat_num_str.isdigit() and item_num_str.isdigit()):
            print("Numbers only!")
            continue
        cat_num = int(cat_num_str)
        item_num = int(item_num_str)

        # map category number
        categories = list(menu.keys())
        if cat_num < 1 or cat_num > len(categories):
            print("Invalid category number!")
            continue
        category = categories[cat_num-1]
        items = menu[category]
        if item_num < 1 or item_num > len(items): 
            print("Invalid item number!")
            continue
        qty = input("Enter quantity: ")
        if not qty.isdigit() or int(qty) <= 0:
            print("Invalid quantity!")
            continue
        qty = int(qty)
        item_name = items[item_num-1]['name']
        price = items[item_num-1]['price']
        if item_name in order:
            order[item_name]['qty'] += qty
        else:
            order[item_name] = {"qty": qty, "price": price}
        print(f"Added {qty} x {item_name} to your order.")

def calculate_bill():
    print("\n--- Order Receipt ---")
    print("{:<25} {:<10} {:<10}".format("Item", "Qty", "Total (PKR)"))
    total_amount = 0
    for name, data in order.items():
        item_total = data['qty'] * data['price']
        total_amount += item_total
        print("{:<25} {:<10} {:<10}".format(name, data['qty'], item_total))
    print("-"*50)
    print(f"Subtotal: PKR {total_amount}")
    
    # Automatic 20% discount
    discount = int(total_amount * 0.2)
    final_total = total_amount - discount
    print(f"Discount (20%): -PKR {discount}")
    print(f"Final Total: PKR {final_total}")
    print("Thank you for visiting our Coffee Shop!")

def main():
    print("Welcome to Pro Terminal Coffee Shop!")
    print("\nCategory Numbers:")
    for i, cat in enumerate(menu.keys(), 1):
        print(f"{i}. {cat}")
    take_order()
    if order:
        calculate_bill()
    else:
        print("No items ordered. Goodbye!")

if __name__ == "__main__":
    main()
