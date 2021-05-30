class Person:




  def __init__(self, fn, ln):
    self.first_name = fn
    self.last_name = ln
    self.address = None

  def set_address(self, address):
    self.address = address

  def __str__(self):
    return f"{self.first_name}{self.last_name}"

class IndividualAccount:

  def __init__(self, sort_code, account_number, owner):
    self.sort_code = sort_code
    self.account_number = account_number
    if type(owner) is Person:
      self.owner = owner
    else:
      self.owner = None
    self.balance = 0

  def get_account_data(self):
    print(f"The account belongs to {self.owner}. the account number is {self.account_number}. The balance is {self.balance}")

  def pay_in(self, money):
    self.balance += money

  def withdraw(self, money):
    self.balance -= money


class SharedAccount:

  def __init__(self, sort_code, account_number):
    self.sort_code = sort_code
    self.account_number = account_number 
    self.owners = []
    self.balance = 0

  def pay_in(self, money):
    self.balance += mony

  def withdraw(self, money):
    self.balance -= money


  def get_account_data(self):
    full_owners = ""
    for person in self.owners:
      full_owners + person + " "
    print(f"This shared account belongs to {full_owners}. The account number is {self.account_number}. The balance is {self.balance}")


p1 = Person("Piotr", "Bednorz")
p2 = Person("Daniel", "Grab")      
p3 = Person("Ovidiu", "Borze")
p4 = Person("Geza", "Smith")

p1.set_address("Nowhere land, W3 HHH")

acc1 = IndividualAccount("120103232", "10-23-56", p2)
acc2 = IndividualAccount("123434243", "11-23-58", p3)
acc3 = IndividualAccount("134343532", "1-14-15", p4)


acc1.get_account_data()
acc1.pay_in(10)
acc2.withdraw(100)
acc3.pay_in(12)

acc1.get_account_data()
acc2.get_account_data()
acc3.get_account_data()