import copy
def _str(_list):
    __list = copy.copy(_list)
    del __list[len(__list) - 1]
    result = str(sec) + 'and ' + str(__list[-1])
    return result
        





