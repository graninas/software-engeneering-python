Domain Specific Languages
Domain Driven Design



Domain - is about business tasks.


DSLs simplify the way we write business logic.


-- http library:

-- METHOD: POST, GET, PUT, DELETE...

def send(url, method:METHOD, payload):
  pass

-- string manipulations:

def split(src, splitter, ...): pass
def group_by(src):
  "Missisippi" -> ["M", "i", "ss", ...]

-----

def withdraw(amount, bankAPI: IBankAPI): pass
def transfer(amount, bank1API, bank2API): pass
def auth(user_creds, bankAPI): pass

def money_validation_process(bankAPI, transaction_reference):
  transaction = get_transaction(bankAPI, transaction_reference)

  is_valid = validate(transaction)
  client = get_client(transaction)
  notify(client)


  if (is_valid):
    set_transaction_status(transaction_reference, VALID)
    log_info("Transaction is valid.")
  else
    set_transaction_status(transaction_reference, NOT_VALID)
    log_info("Transaction is not valid.")


def validate_process(transaction: Transaction):
  ...

# Domain Driven Design


def money_validation_process(bankAPI: IBankAPI, client_notifier: IClientNotifier, transaction_reference, logger: ILogger):
  transaction = bankAPI.get_transaction(transaction_reference)

  is_valid = validate_process(transaction)
  client = transaction.get_client()
  client_notifier.notify(client)

  if (is_valid):
    transaction.set_transaction_status(VALID)
    logger.log_info("Transaction is valid.")
  else
    transaction.set_transaction_status(NOT_VALID)
    logger.log_info("Transaction is not valid.")

# OOP like object (active domain object)
class Transaction:
  def get_client(self): pass
  def set_transaction_status(self): pass


# Inversion of Control
# Dependency injections
...
# TDD (Test Driven Development), BDD (Behavior Driven Development)
# test for money_validation_process:
class Test():
  test_money_validation_process():
    # prepare data: transactions, client_notifier, transaction_reference, DB states
    ...

    money_validation_process(.....)

    # check the results:
    ...

# Domain Specific Languages

1. External DSL (DSL):
  separate syntax
  separate code file

  parser -> translator -> interpreter

  ini-file (configs)
  lua-file (for games)


  Our own syntax sample:

    file validate_process.txn:

      input: transaction(ITransaction)
      ...
      output: True


    file money_validation_process.txn:
    
      include: validate_process
      input: bank_api(IBankAPI)
      input: client_notifier(IClientNotifier)
      input: transaction_reference(ITransactionReference)
      input: ..
      var transaction = call(bank_api, 'get_transaction', [transaction_reference])
      var is_valid = call(validate_process, '')
      ...
      output: is_valid



2. Embedded DSL (eDSL)
    The eDSL is based on the syntax of the host language. Basically, all the scripts are written
    in the host language (like Python), but these scripts are built of a domain-meaning notions.

  * Simple
  * Comprehensive
  * Testable
  * Documented
  ...


  * Imperative style
      All operations are real actions, mutating states, calling external services (do effects immediately)
  * Declarative style
      All the operations are encoded declaratively

      - Declarative with immediate effects: all the operations are happening immediately
      - Declarative with pure declarations: all the operations should be encoded somehow and interpreted lately

class BankAPI:
  pass

class GetTransaction:
  def __init__(bankAPI:BankAPI):
    _bank_api = bankAPI

class GetClient:
  pass

class Notify:
  pass

class LogInfo:
  pass


def money_validation_process_declarative():
  return [
    GetTransaction

  ]


def run_txns_flow(flow:[...]):
  for





# Laziness

  my_func(fact(10), fib(100), fib(200))

  def my_func(arg1, arg2):
