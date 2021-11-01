def meta_decorator(arg):
    def decorator_list(fnc):
        def inner(list_of_tuples):
            return [(fnc(val[0], val[1])) ** power for val in list_of_tuples]
        return inner
    if callable(arg):
        power = 2
        return decorator_list(arg)
    else:
        power = arg
        return decorator_list


@meta_decorator
def add_together(a, b):
    return a + b

# @meta_decorator(3)
# def add_together(a, b):
#     return a + b
