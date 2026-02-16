"""Module providing a function calculating total cart price."""

import logging

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

def format_loggs(): 
    """
    The function `formatLoggs` returns a logging formatter that includes the 
    timestamp, log level, and message.
    """
    return logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


console_handler = logging.StreamHandler()
console_handler.setFormatter(format_loggs())
console_handler.setLevel('DEBUG')
logger.addHandler(console_handler)
info_handler = logging.FileHandler('info.log', 'a', encoding='utf-8')
info_handler.setFormatter(format_loggs())
info_handler.setLevel('INFO')
logger.addHandler(info_handler)
error_handler = logging.FileHandler('errors.log', 'a', encoding='utf-8')
error_handler.setFormatter(format_loggs())
error_handler.setLevel('ERROR')
logger.addHandler(error_handler)


def validate_cart(cart):
    """validate that cart item contains  'price'  'quantity' """
    for item in cart:
        if 'price' not in item or 'quantity' not in item:
            logger.error("Invalid item data: %s", item)
            return False
    return True


def validate_discount(discount, min_n=0, max_n=100): 
    """validate discount data type and value """
    if not isinstance(discount, int): 
        logger.error("Invalid discount data type: %s", discount)
        return False
    if discount < min_n: 
        logger.error("Invalid discount data less than min: %s", discount)
        return False
    if discount > max_n: 
        logger.error("Invalid discount data more than max: %s", discount)
        return False
    return True


def check_float(price, min_n=0, max_n=None): 
    """validate price data type and value """
    if not isinstance(price, float): 
        logger.error("Invalid price data type: %s", price)
        return False
    if price < min_n: 
        logger.error("Invalid price data less than min: %s", price)
        return False
    if max_n: 
        if price > max_n: 
            logger.error("Invalid price data more than max: %s", price)
            return False
    return True


def check_int(quantity, min_n=0, max_n=None): 
    """validate quantity data type and value """
    if not isinstance(quantity, int): 
        logger.error("Invalid quantity data type: %s", quantity)
        return False
    if quantity < min_n: 
        logger.error("Invalid quantity data less than min: %s", quantity)
        return False
    if max_n: 
        if quantity > max_n: 
            logger.error("Invalid quantity data more than max: %s", quantity)
            return False
    return True


def calculate_total(cart, discount=0):
    """ main fucntion calculates cart total price """
    total = 0
    if not validate_cart(cart): 
        return total
    
    for item in cart:
        if check_float(item['price']) and check_int(item['quantity']):
            total += item['price'] * item['quantity']
        else: 
            return 0
      
    if discount:
        if not validate_discount(discount): 
            return 0
        logger.info("Applied discount %s", discount)
        total -= total * (discount / 100)
    
    logger.info("Total calculation complete. Final total: %.2f", total)
        
    return total

# End-of-file (EOF)
