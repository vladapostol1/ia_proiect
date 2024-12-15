import pytest
from recommend_system import generate_recommendations, matches_category, matches_price_range, not_purchased_before

#Date mockup
users_data = [
    {
        "id": "user1",
        "categories": ["electronics", "fitness"],
        "purchase_history": ["mouse"],
        "price_range": [20, 150]
    },
    {
        "id": "user2",
        "categories": ["books"],
        "purchase_history": ["book"],
        "price_range": [10, 50]
    }
]

products_data = [
    {"id": "product1", "name": "mouse", "category": "electronics", "price": 25},
    {"id": "product2", "name": "keyboard", "category": "electronics", "price": 50},
    {"id": "product3", "name": "book", "category": "books", "price": 20},
    {"id": "product4", "name": "dumbbells", "category": "fitness", "price": 50}
]

def test_matches_category():
    user = users_data[0]
    product = products_data[1]
    assert matches_category(user, product) == True 
    product["category"] = "books"
    assert matches_category(user, product) == False 

def test_matches_price_range():
    user = users_data[0]
    product = products_data[1]
    assert matches_price_range(user, product) == True
    product["price"] = 200
    assert matches_price_range(user, product) == False

def test_not_purchased_before():
    user = users_data[0]
    product = products_data[1]
    assert not_purchased_before(user, product) == True
    product["name"] = "mouse"
    assert not_purchased_before(user, product) == False

def test_generate_recommendations():
    user = users_data[0]
    recommendations = generate_recommendations(user, products_data)
    assert "keyboard" or "dumbbells" in recommendations
    assert "mouse" not in recommendations
    assert "book" not in recommendations

def test_generate_recommendations_no_user():
    user = {"id": "unknown", "categories": [], "purchase_history": [], "price_range": [0, 0]}
    recommendations = generate_recommendations(user, products_data)
    assert recommendations == []
