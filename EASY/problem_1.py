'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''


def check_sum(array, k):
    for first in array:
        for second in array:
            if first + second == k:
                return print(f'{first} + {second} = {k}')


def checK_sum_oneliner(array, k):
    return tuple(x for x in array for y in array if x + y == k)

array = [10, 15, 3, 7, 2, 6]
k = 17
k2 = 8

if __name__ == '__main__':
    check_sum(array, k)
    print(checK_sum_oneliner(array,k2))
