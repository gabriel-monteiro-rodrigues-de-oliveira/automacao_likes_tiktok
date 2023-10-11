def is_empty(usr_input):
    return usr_input == ''


def frst_char_at_sign(tt_creator):
    return tt_creator.startswith('@')


def is_int(val):
    return val.isdigit()


def is_less_than(val, max, val_is_int=True):
    if val_is_int:
        return int(val) < max
    return
