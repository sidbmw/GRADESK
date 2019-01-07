def check_string(user_input, v_type, v_length):
    if len(str(user_input)) == v_length and type(user_input) == v_type:
        return True
    else:
        return False


def check_expectation(user_input):
    if list(user_input)[0].isalpha() and list(user_input)[1].isnumeric():  #
        print('it is')
    else:
        print('it is not')


def check_mark(user_input):
    print()
