
def countdown(n):
    if n == 0:
        print("Launch!")
    else:
        print(n)
        countdown (n - 1);
n = int(input("Enter the countdown value: "))
countdown(n)\n

def recursive_linear_search(id_list, target_id, index=0):
    if index >= len(id_list):
        return -1
    if id_list[index] == target_id:
        return index
    return recursive_linear_search(id_list, target_id, index + 1)
if __name__ == "__main__":
    employee_ids = [4021, 1005, 3099, 2045, 5012]
    search_1 = 2045
    search_2 = 9999
    result_1 = recursive_linear_search(employee_ids, search_1)
    result_2 = recursive_linear_search(employee_ids, search_2)
    print(f"Searching for {search_1}: Found at index {result_1}")
    print(f"Searching for {search_2}: Result is {result_2} (Not Found)")\n

def calculate_parcel_arrangements(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_parcel_arrangements(n - 1)
parcels = 7
total_ways = calculate_parcel_arrangements(parcels)
print(f"Total ways to arrange {parcels} parcels: {total_ways}")\n

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def print_fibonacci_series(terms):
    if terms <= 0:
        print("Please enter a positive integer.")
        return
    print(f"The first {terms} terms of the Fibonacci series are:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()  
if __name__ == "__main__":
    n = 10
    print_fibonacci_series(n)\n

def calculate_growth_factor(p, n):
    if n == 0:
        return 1
    else:
        return p * calculate_growth_factor(p, n - 1)
if __name__ == "__main__":
    principal = 10000        
    interest_rate = 0.05     
    years = 10               
    p = 1 + interest_rate
    total_growth_factor = calculate_growth_factor(p, years)
    final_balance = principal * total_growth_factor
    print(f"Principal Investment: ${principal:,.2f}")
    print(f"Growth Factor (p)   : {p}")
    print(f"Duration (n)        : {years} years")
    print(f"Final Balance       : ${final_balance:,.2f}")




