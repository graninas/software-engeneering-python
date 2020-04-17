# 10. Data flow design
# --------------------


class Sink:
    def __init__(self, initial):
        self._initial = initial

    def end(self):
        return self._initial

    def __call__(self, some_arg):
        print('Flow finished')
        return (None, None)

class Pipe:
    def __init__(self, initial):
        self._initial = initial

    def for_each(self, method):
        self._method = method
        self._next = Sink(self._initial)
        return self._next

    def __call__(self, enumerable):
        if (enumerable == None):
            raise Exception("Invalid enumerable")

        if (self._method == None):
            raise Exception("Invalid method")

        for x in enumerable:
            self._method(x)

        return (self._next, None)

class ListSource:
    def __init__(self):
        pass

    def take(self, n):
        self._take_n = n
        self._next = Pipe(self)
        return self._next

    def __call__(self, list_arg):
        print('Flow started.')

        if (list_arg == None):
            raise Exception("Invalid data")

        if (self._take_n != None):
            return (self._next, list_arg[:self._take_n])

        return (None, None)

def runFlow(flow, init_arg):
    next = flow
    arg = init_arg
    while next != None:
        next, arg = next(arg)


flow1 = ListSource().take(3).for_each(lambda x: print(x)).end()


runFlow(flow1, [1,2,3,4,5])
