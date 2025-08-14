def sum_odd_even(numbers):
    sum_odd = 0
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    return sum_odd, sum_even

# Take input from console
nums = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in nums.split()]
odd_sum, even_sum = sum_odd_even(nums)
print(f"Sum of odd numbers: {odd_sum}")
print(f"Sum of even numbers: {even_sum}")