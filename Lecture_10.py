# 10. Data flow design
# --------------------

# Fluent Interface

# class File:
#     def __init__(self, name):
#         try:
#             self._file = open(name)
#         except:
#             self._file = None
#
#     def read(bytes):
#         if (self._file is None):
#             raise Exception('File is invalid')
#
#         return self._file.read(bytes)
#
#     def on_success(self, method):
#         if (self._file is None):
#             return self
#         method(self._file)
#         return self
#
#     def on_fail(self, method):
#         if (self._file is None):
#             method()
#         return self
#
# result1 = File('numbers.txt').read(100)
#
# result = File('numbers.txt')
#     .on_success(lambda file: print(file.read(100)) )
#     .on_fail(lambda: print('File not found'))
#
# ######
#
# class ListSource:
#     def __init__(self, lst):
#         self._lst = lst
#         self._n = None
#
#     def take(self, n):
#         self._n = n
#         return self
#
#     def for_each(self, method):
#         lst = self._lst
#
#         if (self._n is not None):
#             lst = self._lst[self._n:]
#
#         for x in lst:
#             method(x)
#
#         return self
#
# def list_source(lst):
#     return ListSource(lst)
#
# result = list_source([1,2,3,4,5]).take(3).for_each(lambda x: print(x))
# result = list_source([1,2,3,4,5]).for_each(lambda x: print(x))

class Sink:
    def __init__(self, initial):
        self._initial = initial

    def end(self):
        return self._initial

    def __call__(self, arg):
        print('Flow ended.')
        return (None, None)

class Pipe:
    def __init__(self, initial):
        self._initial = initial
        self._take_n = None
        self._drop_n = None
        self._for_each_method = None
        self._filter_pred = None

    def take(self, n):
        self._take_n = n
        self._next = Pipe(self._initial)
        return self._next

    def drop(self, n):
        self._drop_n = n
        self._next = Pipe(self._initial)
        return self._next

    def filter(self, pred):
        self._filter_pred = pred
        self._next = Pipe(self._initial)
        return self._next

    def for_each(self, method):
        self._for_each_method = method
        self._next = Sink(self._initial)
        return self._next

    def __call__(self, lst):
        if (self._drop_n is not None):
            return (self._next, lst[self._drop_n:])

        if (self._take_n is not None):
            return (self._next, lst[:self._take_n])

        if (self._filter_pred is not None):
            lst2 = []
            for x in lst:
                if (self._filter_pred(x)):
                    lst2.append(x)
            return (self._next, lst2)

        if (self._for_each_method is not None):
            for x in lst:
                self._for_each_method(x)
            return (self._next, None)

        raise Exception('Chain is broken')

class ListSource:
    def __init__(self):
        pass

    def set_next(self, pipe):
        self._next = pipe

    def __call__(self, lst):
        print('Flow started.')
        return (self._next, lst)

def runFlow(flow, arg):
    next = flow
    arg2 = arg
    while next is not None:
        next, arg2 = next(arg2)

def list_source():
    lst = ListSource()
    pipe = Pipe(lst)
    lst.set_next(pipe)
    return pipe

# Source -> Pipe
# Pipe -> Pipe (take, drop)
# Pipe -> Sink (for_each)


#       Source        #Pipe   #Pipe                       # Sink
flow1 = list_source().take(3).for_each(lambda x: print(x)).end()

#       Source        #Pipe   #Pipe   #Pipe                        # Sink
flow2 = list_source().drop(2).filter(lambda x: x > 10).take(3).for_each(lambda x: print(x)).end()

# flow11 = list_source().drop(2)
# flow12 = list_source().take(2)

# flow3 = parallel(flow1, flow2)
# flow111 = zip_flows(flow11, flow12).for_each(lambda p1 p2: print(p1))

runFlow(flow1, [1,2,3,4,5])
runFlow(flow1, [1,2,3,4,5,6,7,87,8])
runFlow(flow2, [1,3434,5,565,2,3,4,5,232,5767,23234])
