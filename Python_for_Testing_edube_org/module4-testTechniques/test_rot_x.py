from rot_function import rot_x

##=============================================================================================================================
# 1. Write unit tests for the rot_x() function.
# Use the specified offset values (13, 25, 3) to verify that the function behaves as expected for both encoding and decoding.
##=============================================================================================================================
def text_is_not_empty(text): 
    if text.strip() != '': 
        return text
    else: 
        raise ValueError


def text_is_string(text): 
    if isinstance(text, str): 
        return text
    else: 
        raise TypeError
    

def offset_is_integer(offset): 
    if isinstance(offset, int): 
        return offset
    else: 
        raise TypeError

##=============================================================================================================================
# 2. Implement assertions to verify the correctness of your ROT-X function, ensuring it works as expected for the given sample inputs.
##=============================================================================================================================

# test case 1: encode 1 letter with offset > 1
assert  rot_x('s', 3) == 'v', 's should be encoded as v when offset is 3'
assert  rot_x('v', -3) == 's', 'v should be decoded as s when offset is -3'

# test case 2: encode 3 letters with offset 13 
assert  rot_x('gol', 13) == 'tby', 'gol should be encoded as tby when offset is 13'
assert  rot_x('tby', -13) == 'gol', 'tby should be decoded as gol when offset is -13'

# test case 3: encode Uppercase word with offset 25
assert  rot_x('PASSWORD', 25) == 'ozrrvnqc', 'PASSWORD should be encoded as ozrrvnqc when offset is 25'
assert  rot_x('ozrrvnqc', -25) == 'password', 'ozrrvnqc should be decoded as password when offset is -25'

# test case 4: does not encode/ decode empty string
assert rot_x('', 25) == '', 'encode empty string with offset 25'
assert rot_x('', 13) == '', 'encode empty string with offset 13'
assert rot_x('', 3) == '', 'encode empty string with offset 3'
assert rot_x('', -25) == '', 'decode empty string with offset -25'
assert rot_x('', -13) == '', 'decode empty string with offset -13'
assert rot_x('', -3) == '', 'decode empty string with offset -3'

# test case 5: does not encode/ decode spaces
assert rot_x('   ', 25) == '   ', 'encode spaces string with offset 25'
assert rot_x('   ', 13) == '   ', 'encode spaces string with offset 13'
assert rot_x('   ', 3) == '   ', 'encode spaces string with offset 3'
assert rot_x('   ', -25) == '   ', 'decode spaces string with offset -25'
assert rot_x('   ', -13) == '   ', 'decode spaces string with offset -13'
assert rot_x('   ', -3) == '   ', 'decode spaces string with offset -3'

# test case 6: does not encode numbers
assert rot_x('PAS67RD', 25) == 'ozr67qc', 'encode numbers inside string with offset 25'
assert rot_x('ozr67qc', -25) == 'pas67rd', 'decode numbers inside string with offset -25'

# test case 7: does not encode/ decode special characters
assert rot_x('flñai', 25) == 'ekñzh', 'encode numbers inside string with offset 25'
assert rot_x('ekñzh', -25) == 'flñai', 'encode numbers inside string with offset -25'





