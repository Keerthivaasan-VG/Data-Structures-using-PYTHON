def linear_search(roll_numbers, key):
    for i in range(len(roll_numbers)):
        if roll_numbers[i] == key:
            return i
    return -1

def binary_search(roll_numbers, key):
    roll_numbers.sort()  
    low = 0
    high = len(roll_numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if roll_numbers[mid] == key:
            return mid
        elif roll_numbers[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

roll_numbers = []
n = int(input("Enter the number of students registered for the exam: "))
for i in range(n):
    roll = int(input(f"Enter roll number of student {i + 1}: "))
    roll_numbers.append(roll)


key = int(input("Enter roll number to search: "))

pos1 = linear_search(roll_numbers, key)
if pos1 != -1:
    print(f"Linear Search: Roll number {key} found at position {pos1 + 1}.")
else:
    print(f"Linear Search: Roll number {key} not found.")

pos2 = binary_search(roll_numbers, key)
if pos2 != -1:
    print(f"Binary Search: Roll number {key} found at position {pos2 + 1}.")
else:
    print(f"Binary Search: Roll number {key} not found.")
