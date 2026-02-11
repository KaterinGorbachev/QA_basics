'''
The black box produces a four-character-long output, which the function processes. Each character must match a predefined set based on the character's position. These sets are derived from the rows of keys on a typical 'QWERTY' keyboard layout.

Your objective is to refactor the provided function to follow best practices, making it more readable and maintainable while ensuring it passes all unit tests.

1.Create a new Python file named test_process_values.py and write unit tests for the legacy function process_values(). Use assert statements to verify the function’s behavior with the given test data and cover additional edge cases.
'''


from processor import process_values

# Test case 1: All characters approved
assert process_values('4qfm') == ('4qfm', ''), 'Test case 1 failed.'

# Test case 2: Some characters rejected
assert process_values('w2fm') == ('fm', 'w2'), 'Test case 2 failed.'

# Test case 3: All characters rejected
assert process_values('%&*)') == ('', '%&*)'), 'Test case 3 failed.'

# Test case 4: Spaces rejected
assert process_values('    ') == ('', '    '), 'Test case 4 failed.'

# Test case 5: Uppercase rejected 
assert process_values('QWER') == ('', 'QWER'), 'Test case 5 failed.'

# Test case 6: All characters only from set1, 2-4 characters rejected
assert process_values('1111') == ('1', '111'), 'Test case 6 failed.'

# Test case 7: All characters only from set2, 1, 3-4 characters rejected
assert process_values('qwer') == ('w', 'qer'), 'Test case 7 failed.'

# Test case 8: All characters only from set3, 1, 2, 4 characters rejected
assert process_values('asdf') == ('d', 'asf'), 'Test case 8 failed.'

# Test case 9: All characters only from set4, 1-3 characters rejected
assert process_values('vbnm') == ('m', 'vbn'), 'Test case 9 failed.'

# Test case 10: Uppercase rejected for all sets 
assert process_values('1WAM') == ('1', 'WAM'), 'Test case 10 failed.'






