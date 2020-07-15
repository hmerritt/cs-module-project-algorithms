'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Sort array
    arr.sort()

    # If next value (in a sorted array) is not equal to current -> bingo!
    # Only check even indexes and use last index if none found
    for i, val in enumerate(arr):
        if i == len(arr) - 1 or (i % 2 == 0 and arr[i] != arr[i+1]):
            return val


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
