import random


def matches_category(user, product):
    return product["category"] in user["categories"]

def matches_price_range(user, product):
    return user["price_range"][0] <= product["price"] <= user["price_range"][1]

def not_purchased_before(user, product):
    return product["name"] not in user["purchase_history"]


def generate_recommendations(user, products, max_recommendations=3):
    recommendations = []

    for product in products:
        if (
            matches_category(user, product) and
            matches_price_range(user, product) and
            not_purchased_before(user, product)
        ):
            recommendations.append(product["name"])
    
    if len(recommendations) > max_recommendations:
        recommendations = random.sample(recommendations, max_recommendations)
    
    return recommendations
