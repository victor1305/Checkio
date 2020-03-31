def checkio(number: int) -> int:
    array = []

    for k in str(number):
        array.append(k)

    finalnumber = 1

    for i in range(0, len(array)):

        if int(array[i]) > 0:
            finalnumber *= int(array[i])

    return finalnumber


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
