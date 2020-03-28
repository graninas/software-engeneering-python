8. Error Handling & Resources Management
----------------------------------------

Error handling

# bankAPI library definition for Sber:

class WithdrawMoney:
  def __init__(self, am, is_valid):
    self._amount = am
    self._is_valid = is_valid

  def is_valid(self):
    return self._is_valid

  def validate(self):
    self._is_valid = self._amount > 0

def withdraw (user_account):
  withdraw_money = ... (call external bank services via HTTP)
  return (if withdraw_money == 0 then return 0 else return WithdrawMoney(withdraw_money, True))


def safe_call(method, destruction_method):
  try:
    method()
  except:
    destruction_method()

def withdraw (user_account, bankAPI, amount):
  try:
    conn = bankAPI.connect(user_account)

      try:
        result = bankAPI.withdraw(conn, amount)

        safe_call(labmda: result.validate(), lambda: print('Invalid result'))

        if (result != None):
          result.is_valid()
        else:
          raise Exception('Bang')
      except Exception as ex:
        print(ex.message())

  finally:
    conn.close()

  # External service is down
  # Error, bug in the library
  # The library can throw exceptions
  # Not an appropriate result

  ...

def top_func(bankAPI):
  user_account = get_user_account()

  try:
  result = withdraw(user_account, bankAPI)

  except:


-------

Exception:
* Syntactic construct of the language
  - raise Exception ('Bad thing happened')
  - try:
  - except Exception as ex:
  - finally:
* Unexpected behavior, dangerous, not a part of a domain, emergency situation


Errors:
* Expected, but unwanted


class Natural:
  def __init__(self, n:int):
      if (n <= 0):
        raise Exception('Invalid Argument')
    self._n = n

  def n(self):
    return self._n


class SafeNatural:
  def __init__(self, n:int):
    self._is_valid = n > 0
    if self._is_valid:
      self._n = n
    else:
      self._n = None

  def n(self):
    return self._n

  def is_valid(self):
    return self._is_valid


def safe_compare_eq(n:Natural, val):
  if n.is_valid():
    return SafeBool(n.n() == val)
  else
    SafeBool(None)


def fact(nat:Natural):
  if nat.n() == 1:
    return 1
  next_nat = Natural(nat.n() - 1)
  return fact(next_nat) * nat.n()


- Build a model correct by construction.
- Make invalid states unrepresentable.
- Maybe (optional in C++, Some in Scala...)                 - monads
- Either (expected in C++, Result in Scala, Result C#...)   - monads
- None in Python analogue of null

- Turn a failure into a success list
def withdraw_many (user_account, bankAPI, amount1, amount2, amount3):
    conn = bankAPI.connect(user_account)

    if (conn == None):
      return ('Invalid connection', [])

    result1 = bankAPI.withdraw(conn, amount1)
    result2 = bankAPI.withdraw(conn, amount2)
    result3 = bankAPI.withdraw(conn, amount3)

    result_list = [result1, result2, result3]
    result_filtered = []

    for r in result_list:
      if r != None:
        result_list.add(r)

    return ('', result_filtered)


def do_something():
  list = withdraw_many(...)
