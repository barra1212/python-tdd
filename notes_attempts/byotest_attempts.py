def number_of_evens(numbers):
    return 0

# def test_are_equal(actual, expected):
#     assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

# test_are_equal(number_of_evens([1,2,3,4,5]), 2)




# def test_not_equal(a, b):
#     assert a != b, "Did not expect {0} but got {1}".format(a, b)

# test_not_equal(number_of_evens([1,2,3,4,5]), 2)

# test_not_equal(0, 0)




def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

test_is_in([1], 2)


print("Pass")



# python3 byotest.py