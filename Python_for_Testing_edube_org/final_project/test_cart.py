""" Test scenarios:
- Valid cart with items (white box testing) – write a test that ensures a cart with valid items (e.g., price and quantity specified) returns the correct total.

- Cart missing required fields (black box testing) – write a test to simulate a cart with missing fields (e.g., missing "price" or "quantity") and verify that the function appropriately identifies these invalid items using assertions and logging.

- Edge cases, such as empty carts and 100% discounts – an empty cart and a cart with a 100% discount should both return a total of 0.

Use assert statements to validate these scenarios. """

from cart import calculate_total

# valid test data 
cart_price_quantity_not_zero = [
    { 'price': 25.0, 
    'quantity': 10 }

]
cart_price_quantity_not_zero_multiple_items = [
    { 'price': 25.0, 
    'quantity': 10 }, 
    { 'price': 5.0, 
    'quantity': 10 }

]   
assert calculate_total(cart_price_quantity_not_zero) == 250, 'Invalid result with valid cart one_item'
assert calculate_total(cart_price_quantity_not_zero_multiple_items) == 300, 'Invalid result with valid cart multiple_items'

# invalid test data - missing fields
cart_price_quantity_not_price = [
    { 'precio': 25.0, 
    'quantity': 10 }

]
assert calculate_total(cart_price_quantity_not_price) == 0, 'Test failed: missing price'

cart_price_quantity_not_quantity = [
    { 'precio': 25.0, 
    'cantidad': 10 }

]
assert calculate_total(cart_price_quantity_not_quantity) == 0, 'Test failed: missing quantity'

cart_price_quantity_not_price_first_item_multiple_items = [
    { 'precio': 25.0, 
    'quantity': 10 }, 
    { 'price': 5.0, 
    'quantity': 10 }

]
# test failed here - recomended to add total = 0 after error 
# assert calculate_total(cart_price_quantity_not_price_first_item_multiple_items) == 0, 'Test failed: missing price'
assert calculate_total(cart_price_quantity_not_price_first_item_multiple_items) == 0, 'Test failed: missing price'


cart_price_quantity_not_price_second_item_multiple_items = [
    { 'price': 25.0, 
    'quantity': 10 }, 
    { 'precio': 5.0, 
    'quantity': 10 }

]
assert calculate_total(cart_price_quantity_not_price_second_item_multiple_items) == 0, 'Test failed: missing price'

cart_empty = []
assert calculate_total(cart_empty) == 0, 'Test failed: missing items in a cart'

cart_product_empty = [{}]
assert calculate_total(cart_empty) == 0, 'Test failed: missing items in a cart'

# Edge cases 0
cart_price_zero = [{
    'price': 0.0, 
    'quantity': 10
}]
assert calculate_total(cart_price_zero) == 0, 'Test failed: total != 0'

cart_quantity_zero = [{
    'price': 25.0, 
    'quantity': 0
} ]
discount_100 = 100
assert calculate_total(cart_quantity_zero) == 0, 'Test failed: 100 discount'

#boundary cases around 0

cart_price_positive = [{
    'price': 0.1, 
    'quantity': 10
}]
assert calculate_total(cart_price_positive) == 1, 'Test failed: price 0.1'


cart_quantity_positive = [{
    'price': 10.0, 
    'quantity': 1
}]
assert calculate_total(cart_quantity_positive) == 10, 'Test failed: quantity 1'

discount_boundary_positive_around0 = 1
assert calculate_total(cart_price_quantity_not_zero, discount_boundary_positive_around0) == 247.5, 'Test failed: discount 1'

discount_boundary_less_around100 = 99
assert calculate_total(cart_price_quantity_not_zero, discount_boundary_less_around100) == 2.5, 'Test failed: discount 99' 

discount_boundary_more_around100 = 101
assert calculate_total(cart_price_quantity_not_zero, discount_boundary_more_around100) == 0, 'Test failed: accepts discount more than 100'

discount_boundary_negative_around0 = -1
assert calculate_total(cart_price_quantity_not_zero, discount_boundary_negative_around0) == 0, 'Test failed: accept discount < 0'


cart_price_negative = [{
    'price': -0.1, 
    'quantity': 10
}]
assert calculate_total(cart_price_negative) == 0, 'Test failed: price accept negative'

cart_quantity_negative = [{
    'price': 10.0, 
    'quantity': -1
}]
assert calculate_total(cart_quantity_negative) == 0, 'Test failed: quantity accept negative'
