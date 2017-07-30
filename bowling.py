def score(game):
    result = 0
    frame = 1
    half_number = 1
    for throw_string_index in range(len(game)):
        if game[throw_string_index] == '/':
            result += 10 - last_value
        else:
            result += get_value(game[throw_string_index])
        if frame < 10 and get_value(game[throw_string_index]) == 10:
            if game[throw_string_index] == '/':
                result += get_value(game[throw_string_index+1])
            elif game[throw_string_index] in "xX":
                result += get_value(game[throw_string_index+1])
                if game[throw_string_index+2] == '/':
                    result += 10 - get_value(game[throw_string_index+1])
                else:
                    result += get_value(game[throw_string_index+2])
        last_value = get_value(game[throw_string_index])
        if half_number == 2:
            frame += 1
        if half_number == 1:
            half_number = 2
        else:
            half_number = 1
        if game[throw_string_index] in "xX":
            half_number = 1
            frame += 1
    return result


def get_value(throw_value):
    if throw_value.isnumeric():
        return int(throw_value)
    elif throw_value in "Xx/":
        return 10
    elif throw_value == '-':
        return 0
    else:
        raise ValueError()
