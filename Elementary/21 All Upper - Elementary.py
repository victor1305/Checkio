def is_all_upper(text: str) -> bool:
    # your code here

    if text.isupper():

        return True

    elif text.isspace():

        return True

    elif text.isalpha():

        return True

    elif text == '':

        return True

    else:

        return False




if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")