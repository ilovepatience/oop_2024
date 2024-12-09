def calculate_discounted_price(price, discount_type):
    if discount_type == "new_customer":
        return price - (price * 0.1)
    elif discount_type == "holiday":
        return price - (price * 0.2)
    elif discount_type == "clearance":
        return price - (price * 0.5)
    else:
        return price

final_price = calculate_discounted_price(100, "holiday")
print(final_price)


# DISCOUNT_RATES = {
#     "new_customer": 0.1,
#     "holiday": 0.2,
#     "clearance": 0.5,
# }
#
# def calculate_discounted_price(price, discount_type):
#     discount = DISCOUNT_RATES.get(discount_type, 0)
#     return price - (price * discount)
#
# final_price = calculate_discounted_price(100, "holiday")
# print(final_price)
