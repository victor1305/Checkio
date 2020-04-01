def nearest_value(values: set, one: int) -> int:

    # your code here

    numbersList = list(values)

    positiveDifferences = []

    negativeDifferences = []

    for i in numbersList:

        difference = one - int(i)

        if difference <= 0:

            negativeDifferences.append(difference)

        if difference > 0:

            positiveDifferences.append(difference)

    if negativeDifferences != []:

        negativeMinDifference = max(negativeDifferences)

    else:

        negativeMinDifference = max(positiveDifferences)

    if positiveDifferences != []:

        positiveMinDifference = min(positiveDifferences)

    else:

        positiveMinDifference = min(negativeDifferences)

    absoluteNegativeMinDifference = abs(negativeMinDifference)

    if absoluteNegativeMinDifference == positiveMinDifference:

        number = one - positiveMinDifference

    elif absoluteNegativeMinDifference < abs(positiveMinDifference):

        number = one + absoluteNegativeMinDifference

    else:

        number = one - positiveMinDifference

    return number


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")