9. Resources Management
-----------------------


# number.txt:
# 1 2 3   5435      22    , sihfskfjes

def some():
  file = open('./numbers.txt', 'r')

  content = file.read_all()

  num_strs = content.split(' ')

  nums = []
  for num_str in num_strs:
    nums.append(int(num_str))

  file.close()

def something_else():
  while True:
    some()


- Not hold the resource more than it's needed
def some():
  file = open('./numbers.txt', 'r')
  content = file.read_all()
  file.close()

  num_strs = content.split(' ')

  nums = []
  for num_str in num_strs:
    nums.append(int(num_str))


- OOP constructors and destructors
- RAII - Resource Aquisition is Instantiation
- Monads

class FileResource:
    def __init__(self, file_path):
        self.__file = None
        try:
            self.__file = open(file_path)
        except Exception as ex:
            self.__file = None

    def __del__(self):
        if (self.__file == None):
            pass
        else:
            self.__file.close()

    def read_all(self):
        ...

def some():
    resource = FileResource('./numbers.txt')

    contents = resource.read_all()
    num_strs = content.split(' ')

    nums = []
    for num_str in num_strs:
        nums.append(int(num_str))
    return nums

def something_else():
    nums = some()

Problems:
* Double freeing
* Race conditions
* Exceptions

Resource:
* Files
* Memory
* Thread

def some():
    with open('./numbers.txt') as file:
        contents = file.read_all()
