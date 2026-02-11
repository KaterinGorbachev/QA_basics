'''
Refactor the provided function process_values(blackbox_output) to follow best practices, making it more readable and maintainable while ensuring it passes all unit tests.

2. Refactor the legacy code to extract the repeated validation logic into a helper function called process_single_value(). Verify that the function still passes all the unit tests after this change.

3. Further refactor the code by introducing a loop to handle the character processing, replacing the repeated function calls. 

4. Review your refactored code and optimize it for better readability and maintainability. Ensure all test cases still pass and the code adheres to Pythonic practices.


'''
def process_single_value(value, value_set, approved: list, rejected: list): 
    if value in value_set: 
        approved.append(value)
    else: 
        rejected.append(value)


def process_values(blackbox_output):
    sets = ('1234567890', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm')
    approved, rejected = [], []

    for char, valid_set in zip(blackbox_output, sets):
        process_single_value(char, valid_set, approved, rejected)

    return ''.join(approved), ''.join(rejected)