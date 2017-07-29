def score(game):
    result = 0
    frame = 1
    half_number = 1
    for string_index in range(len(game)):
        if game[string_index] == '/':
            result += 10 - last
        else:
            result += get_value(game[string_index])
        if frame < 10 and get_value(game[string_index]) == 10:
            if game[string_index] == '/':
                result += get_value(game[string_index+1])
            elif game[string_index] == 'X' or game[string_index] == 'x':
                result += get_value(game[string_index+1])
                if game[string_index+2] == '/':
                    result += 10 - get_value(game[string_index+1])
                else:
                    result += get_value(game[string_index+2])
        last = get_value(game[string_index])
        if half_number == 2:
            frame += 1
        if half_number == 1:
            half_number = 2
        else:
            half_number = 1
        if game[string_index] == 'X' or game[string_index] == 'x':
            half_number = 1
            frame += 1
    return result


def get_value(value):
    if value.isnumeric():
        return int(value)
    elif value == 'X' or value == 'x' or value == '/':
        return 10
    elif value == '-':
        return 0
    else:
        raise ValueError()
