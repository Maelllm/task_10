def time_delay(function):
    from datetime import datetime
    def wrapper(arg):
        function_start = datetime.now()
        result = function(arg)
        function_end = datetime.now()
        print(f' {result} was calculated in {function_end - function_start} seconds')

        return result

    return wrapper


@time_delay
def func(v):
    t = [i ** 2 for i in range(v)]
    return t


func(5)


def greetings(function):
    def wrapper(arg):
        print("hello, thank you for using me")
        function(arg)
        return print(f'Your result if {function(arg)}')

    return wrapper


@greetings
def func_2(v):
    return v ** 2


func_2(45)


def goodbye(function):
    def wrapper(arg):
        print(function(arg))
        print("You can always count on me")
        return

    return wrapper

@goodbye
def func_3(v):
    k = v**2 -4*v
    return k

func_3(24)