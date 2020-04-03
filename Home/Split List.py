def split_list(items: list) -> list:

    # your code here

    if len(items) % 2 == 0:

        halfLen = int(len(items)/2)

        firstList = items[0:halfLen]
        secondList = items[halfLen:]

        finalList= [firstList , secondList]

    else:

        halfLen = int(len(items) / 2)

        firstList = items[0:halfLen + 1]
        secondList = items[halfLen +1 :]

        finalList = [firstList, secondList]


    return finalList


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
