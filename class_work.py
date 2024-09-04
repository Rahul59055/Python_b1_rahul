##Write a function that takes one input argument and returns it's sum , cumulative sum, average, min & max using for loops
def calculate_stats(numbers):
    
    if not numbers:
        raise ValueError("The input list must not be empty.")

    total_sum = 0
    cumulative_sum = []
    min_value = float('inf')
    max_value = float('-inf')
    
    for num in numbers:
        total_sum += num
        cumulative_sum.append(total_sum)
        
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    
    average = total_sum / len(numbers)
    
    return {
        'sum': total_sum,
        'cumulative_sum': cumulative_sum,
        'average': average,
        'min': min_value,
        'max': max_value
    }

# Example usage:
lst=[1, 2, 3, 4]
stats = calculate_stats(lst)
print(stats)

 # write a program to take n inputs from user and store them as a list.
# case1: n is defined by user, 
# case2: user can inter number as per their requirements

def FUNC(n):
    l1=[]
    for i in range(0,n):
        ele=int(input("enter a number :"))
        l1.append(ele)
    print(l1)
n=int(input("enter the size of the list: "))
FUNC(n)