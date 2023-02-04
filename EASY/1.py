from random import randint

'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''


def check_sum(array, k):

    for first in array:
        for second in array:
            if first + second == k:
                return print(f'{first} + {second} = {k}')


array = [10, 15, 3, 7]
k = 17

if __name__ == '__main__':
    check_sum(array, k)
