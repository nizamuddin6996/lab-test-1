# Read input from the user
input_str = input("Enter integers separated by spaces: ")
nums = list(map(int, input_str.split()))

# Remove duplicates using set, then sort the result
unique_sorted = sorted(set(nums))

# Print the result
print(unique_sorted)