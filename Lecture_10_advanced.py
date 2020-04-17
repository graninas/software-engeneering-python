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
        self._next = None
        self._take_n = None
        self._drop_n = None
        self._for_each_method = None

    def take(self, n):
        self._take_n = n
        self._next = Pipe(self._initial)
        return self._next

    def drop(self, n):
        self._drop_n = n
        self._next = Pipe(self._initial)
        return self._next

    def for_each(self, method):
        self._for_each_method = method
        self._next = Sink(self._initial)
        return self._next

    def __call__(self, enumerable):
        if (enumerable == None):
            raise Exception("Invalid enumerable")

        if (self._for_each_method != None):
            for x in enumerable:
                self._for_each_method(x)
            return (self._next, None)

        if (self._take_n != None):
            return (self._next, enumerable[:self._take_n])

        if (self._drop_n != None):
            return (self._next, enumerable[self._drop_n:])

        raise Exception('Flow is incomplete.')

class ListSource:
    def __init__(self):
        self._next = None
        self._take_n = None
        self._drop_n = None
        self._for_each_method = None

    def take(self, n):
        self._take_n = n
        self._next = Pipe(self)
        return self._next

    def drop(self, n):
        self._drop_n = n
        self._next = Pipe(self)
        return self._next

    def for_each(self, method):
        self._for_each_method = method
        self._next = Sink(self)
        return self._next

    def __call__(self, enumerable):
        print('Flow started.')

        if (enumerable == None):
            raise Exception("Invalid data")

        if (self._for_each_method != None):
            for x in enumerable:
                self._for_each_method(x)
            return (self._next, None)

        if (self._take_n != None):
            return (self._next, enumerable[:self._take_n])

        if (self._drop_n != None):
            return (self._next, enumerable[self._drop_n:])

        raise Exception('Flow is incomplete.')

def runFlow(flow, init_arg):
    next = flow
    arg = init_arg
    while next != None:
        next, arg = next(arg)


flow1 = ListSource().take(3).for_each(lambda x: print(x)).end()
flow2 = ListSource().drop(2).take(3).for_each(lambda x: print(x)).end()


runFlow(flow1, [1,2,3,4,5])
runFlow(flow2, [1,2,3,4,5])
