def is_strike(char):
    if char == 'X' or char == 'x':
        return True
    return False


def is_spare(char):
    if char == '/':
        return True
    return False


def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):

        current_frame, current_frame_value = game[i], get_value(game[i])

        # calculating result/score
        if is_spare(current_frame):
            result += 10 - last
        else:
            result += current_frame_value
        if frame < 10 and current_frame_value == 10:

            next_frame_value_1 = get_value(game[i+1])
            next_frame_2, next_frame_value_2 = game[i+2], get_value(game[i+2])

            if is_spare(current_frame) or is_strike(current_frame):
                result += next_frame_value_1
                if is_strike(current_frame) and is_spare(next_frame_2):
                    result += 10 - next_frame_value_1
                elif is_strike(current_frame):
                    result += next_frame_value_2
        last = current_frame_value

        # frame stepping
        if not in_first_half:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if is_strike(current_frame):
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif is_strike(char) or is_spare(char):
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
