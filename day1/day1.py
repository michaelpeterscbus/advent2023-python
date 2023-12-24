def sum_callibration_values(file_path):
    lines = open(file_path, 'r').readlines()
    sum = 0
    for line in lines:
        left, right = 0, len(line) - 1
        digit_1, digit_2 = -1, -1
        while digit_1 == -1 or digit_2 == -1:
            if digit_1 == -1 and line[left].isdigit():
                digit_1 = int(line[left])
            if digit_2 == -1 and line[right].isdigit():
                digit_2 = int(line[right])
            left += 1
            right -= 1
        sum += digit_1 * 10 + digit_2
    return sum

def sum_with_letters(file_path):
    nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    lines = open(file_path, 'r').readlines()
    sum = 0
    for line in lines:
        left, right = 0, len(line) - 1
        digit_1, digit_2 = -1, -1
        while digit_1 == -1 or digit_2 == -1:
            if digit_1 == -1:
                if line[left].isdigit():
                    digit_1 = int(line[left])
                else:
                    digit_1 = _check_for_num_str(digit_1, left, line, nums)
            if digit_2 == -1:
                if line[right].isdigit():
                    digit_2 = int(line[right])
                else:
                    digit_2 = _check_for_num_str(digit_2, right, line, nums)
            left += 1
            right -= 1
        sum += digit_1 * 10 + digit_2
    return sum

def _check_for_num_str(digit_1, left, line, nums):
    for num in nums:
        if line[left:len(line)].startswith(num):
            digit_1 = nums[num]
            break
    return digit_1

print(sum_callibration_values('input/testInput.txt'))
print(sum_callibration_values('input/input.txt'))

print(sum_with_letters('input/testInput2.txt'))
print(sum_with_letters('input/input.txt'))