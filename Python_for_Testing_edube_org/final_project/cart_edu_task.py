import logging


## tasks involve analyzing, testing, refactoring, and logging key events for better traceability
#================
# Use a static analysis tool like pylint or flake8 to identify issues in the provided code. 
# Document the warnings and suggestions, and decide which ones to address during refactoring.
# used comand: pylint cart.py --msg-template="{path}({line}): [{msg_id}{obj}] {msg}" > pylint_output_visualstudio.txt
#==================


###--------------loggers-----------------------
# The code `logger = logging.getLogger(__name)` is creating a logger object named `logger` using the
# `logging` module in Python. The `__name__` variable refers to the name of the current module. By
# using this, each module can have its own logger with a unique name.
# logging levels https://docs.python.org/3/library/logging.html#logging-levels 
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


###--------------------------------
def format_loggs(): 
    """
    The function `formatLoggs` returns a logging formatter that includes the timestamp, log level, and
    message.
    """
    return logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
###-----------------------


def console_logger(logger): 
    """ Setting up a console handler for logging in Python. 
    :param logger: The `logger` parameter in the `infoLogger` function is an instance of the
    `logging.Logger` class from the Python `logging` module. It is used to configure and manage logging
    in your Python application""" 
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(format_loggs())
    console_handler.setLevel('DEBUG')
    logger.addHandler(console_handler)

# Setting up a console handler for logging. 
console_logger(logger)


###-----------------------
def info_logger(logger): 
    """
    The `infoLogger` function adds an INFO level file handler to a logger object.
    :param logger: The `logger` parameter in the `infoLogger` 
    function is an instance of the
    `logging.Logger` class from the Python `logging` module. It is used to configure and manage logging
    in your Python application
    """
    info_handler = logging.FileHandler('info.log', 'a', encoding='utf-8')
    info_handler.setFormatter(format_loggs())
    info_handler.setLevel('INFO')
    logger.addHandler(info_handler)

# Setting up a file handler for INFO level logging in Python.
info_logger(logger)


###--------------------------
def errorLogger(logger): 
    """
    The `errorLogger` function adds an ERROR level file handler to a logger object.
    :param logger: The `logger` parameter in the `infoLogger` function is an instance of the
    `logging.Logger` class from the Python `logging` module. It is used to configure and manage logging
    in your Python application
    """
    error_handler = logging.FileHandler('errors.log', 'a', encoding='utf-8')
    error_handler.setFormatter(format_loggs())
    error_handler.setLevel('ERROR')
    logger.addHandler(error_handler)

# Setting up a file handler for ERROR level logging in Python.
errorLogger(logger)


#=================================================================================================================
## pylint errors
## cart.py(97): [C0304] Final newline missing
## Missing function or method docstring - for function description
##==================================================================
## flake8 errors: 2 blanck lines before function
## edube provided code 
def calculate_total_edube(cart, discount=0):
    total = 0
    for item in cart:
        if 'price' in item and 'quantity' in item:
            total += item['price'] * item['quantity']
        else:
            logger.error("Invalid item data: %s", item)
    if discount:
        total -= total * (discount / 100)
        if total < 0: 
            logger.error("Invalid discount data: %s", discount)
    return total


def validate_cart_edube(cart):
    for item in cart:
        if 'price' not in item or 'quantity' not in item:
            return False
    return True


#refactored code 

def validate_cart(cart):
    for item in cart:
        if 'price' not in item or 'quantity' not in item:
            logger.error("Invalid item data: %s", item)
            return False
    return True

def validate_discount(discount, min_n=0, max_n=100): 
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
    if not isinstance(price, float): 
        logger.error("Invalid price data type: %s", price)
        return False
    if price < min_n: 
        logger.error("Invalid price data less than min: %s", price)
        return False
    if max: 
        if price > max_n: 
            logger.error("Invalid price data more than max: %s", price)
            return False
    return True

def check_int(quantity, min_n=0, max_n=None): 
    if not isinstance(quantity, int): 
        logger.error("Invalid quantity data type: %s", quantity)
        return False
    if quantity < min_n: 
        logger.error("Invalid quantity data less than min: %s", quantity)
        return False
    if max: 
        if quantity > max_n: 
            logger.error("Invalid quantity data more than max: %s", quantity)
            return False
    return True


def calculate_total(cart, discount=0):
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
        total -= total * (discount / 100)
        logger.info("Applied discount %s%", discount)
    
    logger.info("Total calculation complete. Final total: %.2f", total)
        
    return total




# End-of-file (EOF)
