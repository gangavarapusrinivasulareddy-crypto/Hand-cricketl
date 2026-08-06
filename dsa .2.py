'''n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
key = int(input("Enter the element to search: "))
found = False
for i in range(n):
    if arr[i] == key:
        print(f"Element found at position {i + 1}")
        found = True
        break
if not found:
    print("Element not found")
'''

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))
key = int(input("Enter the element to search: "))
if arr == sorted(arr):
    print("The given array is already sorted.")
else:
    print("The given array is unsorted.")
    arr.sort()
    print("Sorted array:", arr)
result = binary_search(arr, key)
if result != -1:
    print(f"Element {key} found at position {result + 1} in the sorted array.")
else:
    print("Element not found.")

