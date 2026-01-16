nums = [1, 2, 3, 4]
max_product = 1

for num in nums:
    max_product *= num

print(max_product)
num_product = []

for i in range(len(nums)):
    num_product.append(int(max_product / nums[i]))

print(num_product)