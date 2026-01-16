nums = [100, 4, 200, 1, 3, 2]

def check_longest_consequitive_seq(nums):
    longest_sequence = []
    num_set = set(nums)
    longest_streak = 0

    for num in nums:
        current_sequence = []
        if num-1 not in num_set:
            current_sequence.append(num)
            current_streak = 1

            while num+1 in num_set:
                current_sequence.append(num+1)
                current_streak += 1
                num += 1

            longest_streak = max(longest_streak, current_streak)
            if longest_streak > current_streak:
                longest_sequence = longest_sequence
            else:
                longest_sequence = current_sequence

    print(longest_sequence)
    print(longest_streak)

check_longest_consequitive_seq(nums)