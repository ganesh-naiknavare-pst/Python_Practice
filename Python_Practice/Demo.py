def add_three_numbers():
    """Function to take three integers as input and return their sum."""
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    
    return num1 + num2 + num3

# Calling the function and displaying the result
result = add_three_numbers()
print("The sum of the three numbers is:", result)




# It returns location of x in given array arr
def binarySearch(arr, low, x):

    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
