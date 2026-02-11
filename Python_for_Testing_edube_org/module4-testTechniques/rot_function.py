def rot_x(text, offset):
    lower_cases = 'abcdefghijklmnopqrstuvwxyz'
    lc_len = len(lower_cases)
    new_text = []
    for char in text.lower():
        if char not in lower_cases:
            new_text.append(char)
        else:
            new_char_index = (lower_cases.index(char) + offset) % lc_len
            new_text.append(lower_cases[new_char_index])

    return ''.join(new_text)

# print('chicken encoded sounds like: ', rot_x('chicken', 3))
# print('fklfnhq decoded sounds like: ', rot_x('fklfnhq', -3))
