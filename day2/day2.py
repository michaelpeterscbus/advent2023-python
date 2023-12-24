color_counts = {'red': 12, 'green': 13, 'blue': 14}
def sum_game_ids(file_path):
    lines = open(file_path, 'r').readlines()
    sum = 0
    for line in lines:
        is_possible, game_num = _game_is_possible(line)
        if is_possible:
            sum += game_num
    return sum

def sum_powers(file_path):
    lines = open(file_path, 'r').readlines()
    sum = 0
    for line in lines:
        sum += _get_power(line)
    return sum


def _game_is_possible(line):
    arr = line.split(':')
    game_num = int(arr[0].split(' ')[1])
    turns = arr[1].split(';')
    for turn in turns:
        cubes = turn.split(', ')
        for cube in cubes:
            count, color = cube.strip().split(' ')
            if color_counts[color] < int(count):
                return False, game_num
    return True, game_num

def _get_power(line):
    min_color_counts = {'red': 0, 'green': 0, 'blue': 0}
    arr = line.split(':')
    turns = arr[1].split(';')
    for turn in turns:
        cubes = turn.split(', ')
        for cube in cubes:
            count, color = cube.strip().split(' ')
            if min_color_counts[color] < int(count):
                min_color_counts[color] = int(count)
    return min_color_counts['green'] * min_color_counts['red'] * min_color_counts['blue']

print(sum_game_ids('input/testInput.txt'))
print(sum_game_ids('input/input.txt'))

print(sum_powers('input/testInput.txt'))
print(sum_powers('input/input.txt'))