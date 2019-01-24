# author: Mike Dong, Late December
# version: 3.1


def check_string(user_input, v_type, v_max):
    if v_type == 'str':
        if len(str(user_input)) <= v_max and str(type(user_input)) == '<class \'' + v_type + '\'>':
            return True
        else:
            return False
    if v_type == 'int':
        if int(user_input) <= int(v_max) and user_input.isnumeric():
            return True
        else:
            return False


def check_expectation(user_input):
    if list(user_input)[0].isalpha() and list(user_input)[1].isnumeric():  #
        return True
    else:
        return False


def check_mark(user_input):
    if list(user_input)[0] == '1' or list(user_input)[0] == '2' or list(user_input)[0] == '3' or list(user_input)[0] == '4' \
            or user_input == 'R' or user_input == 'INC':

        if len(user_input) == 2:
            if list(user_input)[1] == '+' or list(user_input)[1] == '-':
                return True
            else:
                return False

        if len(user_input) == 3 and list(user_input)[0].isnumeric():
            if list(user_input)[1] == '+' or list(user_input)[1] == '-':
                if list(user_input)[2] == list(user_input)[1]:
                    return True
                else:
                    return False
            else:
                return False

        if (len(user_input) == 4 or len(user_input) == 5) and list(user_input)[0].isnumeric() and list(user_input)[3].isnumeric() and \
                list(user_input)[2] == '/':
            if int(list(user_input)[0]) + 1 == int(list(user_input)[3]) and list(user_input)[1] == '+' and list(user_input)[4] == '-':
                return True
            if list(user_input)[0] == list(user_input)[3] and len(list(user_input)) == 4:
                return True
            else:
                return False
        return True
    else:
        return False
