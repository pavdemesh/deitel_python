# Exercise 10_02 from Deitel: Intro to Python and CS

from decimal import Decimal

"""Modify Section 10.2.2’s Account class to provide read-only properties for the name and balance. 
Rename the class attributes with single leading underscores. 
Re-execute Section 10.2.2’s IPython session to test your updated class. 
To show that name and balance are read-only, try to assign new values to them"""

"""Account class definition."""


class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self._name = name
        self._balance = balance

    # define a read-only property for name
    @property
    def name(self):
        return self._name

    # define a read-only property for balance
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self._balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account."""

        if amount > self._balance:
            raise ValueError('amount to withdraw must not be greater than the balance')

        if amount < Decimal('0.00'):
            raise ValueError('amount to withdraw must be positive')

        self._balance -= amount


# testing by creating an object and reading its properties
acc1 = Account(name='John Snow', balance=Decimal('75.00'))
print(acc1.balance)
print(acc1.name)

# trying to set name to another value will cause an error since name is read-only property
# acc1.name = 'Siddhartha'
