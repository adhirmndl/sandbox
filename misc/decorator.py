def outer(some_func):
    def inner():
        print "decorating some func"
        ret = some_func()
        return ret + 1
    return inner

def foo():
    return 1

