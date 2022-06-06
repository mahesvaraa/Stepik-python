def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    try:
        res = [i for i in data]
        arr = [[res[0]]]
        j = 0
        for i in range(1, len(res)):
            if res[i] - res[i - 1] == 1:
                arr[j].append(res[i])
            else:
                j += 1
                arr.extend([[res[i]]])
        for i in range(len(arr)):
            arr[i] = (arr[i][0], arr[i][-1])

        return iter(arr)
    except:
        return iter([])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    res = create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))
    assert hasattr(res, '__iter__'), "your function should return the iterator object"
    assert hasattr(res, '__next__'), "your function should return the iterator object"

    assert list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
        (1, 5), (7, 8), (12, 12)], "First"
    assert list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
        (1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
    print(create_intervals([]))
