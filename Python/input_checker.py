def check_string(user_input, v_type, v_max):
    if v_type == 'str':
        if len(str(user_input)) <= v_max and str(type(user_input)) == '<class \'' + v_type + '\'>':
            return True
        else:
            return False
    if v_type == 'int':
        if int(user_input) <= v_max and str(type(user_input)) == '<class \'' + v_type + '\'>':
            return True
        else:
            return False


def check_expectation(user_input):
    if list(user_input)[0].isalpha() and list(user_input)[1].isnumeric():  #
        print('it is')
    else:
        print('it is not')


def check_mark(user_input):
    if list(user_input)[0].isalpha() or user_input == 'R':
        if len(user_input) == 2:
            if list(user_input)[1] == '+' or list(user_input)[1] == '-':
                return True
        if len(user_input) == 3:
            if list(user_input)[1] == '+' or list(user_input)[1] == '-':
                if list(user_input)[2] == '+' or list(user_input)[2] == '-':
                    return True
        return True

