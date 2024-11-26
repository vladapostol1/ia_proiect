import json
from recommend_system import generate_recommendations

#Fisiere mockup pentru DB
USERS_DB = "users.json"
PRODUCTS_DB = "products.json"

#Scriere citire DB
def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_data(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def add_user():
    users = load_data(USERS_DB)
    user_id = input("user_id: ")
    
    new_user = {
        "id": user_id,
        "categories": [],
        "purchase_history": [],
        "price_range":[]
    }
    users.append(new_user)
    save_data(USERS_DB, users)
    print("New user added")

def add_product():
    products = load_data(PRODUCTS_DB)
    product_id = input("product_id: ")
    name = input("product_name: ")
    category = input("product_category: ")
    price = float(input("product_price: "))
    
    new_product = {
        "id": product_id,
        "name": name,
        "category": category.strip(),
        "price": price
    }
    products.append(new_product)
    save_data(PRODUCTS_DB, products)
    print("New product added")

def add_purchase():
    users = load_data(USERS_DB)
    products = load_data(PRODUCTS_DB)
    
    user_id = input("Who did the purchase(user_id): ")
    user = next((u for u in users if u["id"] == user_id), None)
    
    if not user:
        print("The user was not found")
        return
    
    product_id = input("What did they buy(product_id): ")
    product = next((p for p in products if p["id"] == product_id), None)
    
    if not product:
        print("The product was not found")
        return
    
    user["purchase_history"].append(product["name"])
    
    if not user["price_range"]:
        price = product["price"]
        user["price_range"] = [price * 0.8, price * 1.2]
    else:
        min_price, max_price = user["price_range"]
        price = product["price"]
        user["price_range"] = [min(min_price, price * 0.8), max(max_price, price * 1.2)]
    
    if product["category"] not in user["categories"]:
        user["categories"].append(product["category"])
    
    save_data(USERS_DB, users)
    print("New purchase added and user preferences updated!")


def recommend():
    users = load_data(USERS_DB)
    products = load_data(PRODUCTS_DB)
    
    user_id = input("Reccommend for user(user_id): ")
    user = next((u for u in users if u["id"] == user_id), None)
    
    if not user:
        print("The user id was not found")
        return
    
    recommendations = generate_recommendations(user, products)
    print("Recommendations:", recommendations)

def main():
    while True:
        print("\nOpțiuni:")
        print("1. Add user")
        print("2. Add product")
        print("3. New purchase")
        print("4. Recommend")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            add_product()
        elif choice == "3":
            add_purchase()
        elif choice == "4":
            recommend()
        elif choice == "0":
            print("Byeeeee!")
            break
        else:
            print("You need to choose a valid option!")

if __name__ == "__main__":
    main()
