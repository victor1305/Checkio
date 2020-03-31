def is_all_upper(text: str) -> bool:
    # your code here

    text2 = text.replace(" ", "")

    if text2.isalpha():

        if text2.isupper():

            return True

        else:

            return False

    else:

        return True



if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")