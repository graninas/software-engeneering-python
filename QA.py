Monads, Functors
----------------

Functional Programming
- Statically typed FP
- Dynamicly typed langs

def function1(x):
  # read file
  value_from_file = ...
  return x + 1 + value_from_file

def function2(y):
  return y * 2


def combination(x):
  # return function2(function1(x))

  result = function1(x)
  return function2(result)

------------------

impure calls pure is okay
pure calls impure - pure becomes impure

Maybe, Either

------------------

class Maybe:

  # result can be None
    def __init__(self, result):
        self.__result = result

    def is_none(self):
        return (self.__result == None)

    def get_value(self):
        return self.__result

def divide_unsafe(x, y):
    if (y == 0):
        raise Exception("Y is zero")
    return x / y

def log_unsafe(x, base):
    if (x <= 0):
        raise Exception("X is less or equal to 0")
    return log(x, base)

# ------

def on_success(x, pred, op):
    if (not pred(x)):
        return Maybe(None)
    return Maybe(op(x))

def log_safe(x, base) -> Maybe:
    #if (x <= 0):
    #    return Maybe(None)
    #return Maybe(log(x, base))

    return on_success(x, x <= 0, lambda y: log(y, base))


def on_success2(pred, op):
    if (not pred()):
        return Maybe(None)
    return Maybe(op())

def log_safe2(x, base) -> Maybe:
    #if (x <= 0):
    #    return Maybe(None)
    #return Maybe(log(x, base))

    return on_success2(lambda: x <= 0, lambda: log(x, base))


def divid_safe(x, y) -> Maybe:
  if (y == 0):
     return Maybe(None)
  return Maybe(x / y)

def bind(m1: Maybe, func) -> Maybe:
#    return on_success(m1.get_value(), lambda m: m.is_none(), lambda m: func(m))

    if (m1.is_none()):
        return Maybe(None)
    else:
        return func(m1.get_value())


class Either

def some():
    result1 = divide_safe(1, -3)
    if (result1.is_none()):
        print("Wrong operation")
    else:
        result2 = log_safe(result1.get_value(), 10)
        if (result2.is_none()):
            print("Wrong operation")
        else:
            print(result2.get_value())


    mresult1 : Maybe = divide_safe(1, 3)
    mresult2 : Maybe = bind(mresult1, lambda res: log_safe(res, 10))
    mresult3 : Maybe = bind(mresult2, lambda res: log_safe(res, 2))

    if (mresult3.is_none()):
        print("Wrong operation")
    else:
        print(mresult3.get_value())



    try:
        r1 = divide_unsafe(1, -3)
        r2 = log_unsafe(r1, 10)
    ...


calc_result :: Maybe Float
calc_result =
    bind (divid_safe 1 3)
        (\res1 -> bind (log_safe res1)
            (\res2 -> log_safe res2)
        )


calc_result :: Maybe Float
calc_result =
    (divid_safe 1 3) >>=
        (\res1 -> log_safe res1 >>= (\res2 -> log_safe res2))


calc_result :: Maybe Float
calc_result = do
    result1 <- divid_safe 1 3
    result2 <- log_safe result1
    result3 <- log_safe result2
    return result3

some :: IO ()
some = do
