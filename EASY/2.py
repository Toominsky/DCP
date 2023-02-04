'''Given an array of integers, return a new array such that each 
element at index i of the new array is the product of all the 
numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can’t use division?'''

def product(array):
    products_array = []
    for i in range(len(array)):
        result = 1
        for x in range(len(array)):
            if x != i:
                result = result * array[x]
        products_array.append(result)
    return products_array
        

array = [1, 2, 3, 4, 5]

print(product(array))