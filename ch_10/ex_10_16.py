# Exercise 10_16 from Deitel: Intro to Python and CS

"""
Create an inheritance hierarchy that a bank might use to represent customer bank accounts.
All customers at this bank can deposit money into their accounts and withdraw money from their accounts.
More specific types of accounts also exist.

Savings accounts, for instance, earn interest on the money they hold.
Checking accounts, on the other hand, don’t earn interest and charge a fee per transaction.

Start with class Account from this chapter and create two subclasses SavingsAccount and CheckingAccount.

A SavingsAccount should also include a data attribute indicating the interest rate.
Its calculate_interest method should return the Decimal result of multiplying the interest rate by the account balance.
SavingsAccount should inherit methods deposit and withdraw without redefining them.

A CheckingAccount should include a Decimal data attribute that represents the fee charged per transaction.
Class CheckingAccount should override methods deposit and withdraw
so that they subtract the fee from the account balance whenever either transaction is performed successfully.
CheckingAccount’s versions of these methods should invoke the base-class Account versions to update the account balance.
CheckingAccount’s withdraw method should charge a fee only if money is withdrawn
(that is, the withdrawal amount does not exceed the account balance).

Create objects of each class and tests their methods.
Add interest to the SavingsAccount object by invoking its calculate_interest method,
then passing the returned interest amount to the object’s deposit method.
"""

from decimal import Decimal


class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account."""

        if amount > self.balance:
            raise ValueError('amount to withdraw must not be greater than the balance')

        if amount < Decimal('0.00'):
            raise ValueError('amount to withdraw must be positive')

        self.balance -= amount


class SavingsAccount(Account):
    """ Class SavingsAccount for maintaining savings account data.
    SavingsAccount is based on the Account class. Inherits all methods and attributes.
    Implements additional attribute interest_rate and additional method calculate_interest.
    """

    def __init__(self, name, balance, interest_rate):
        """Initialize a SavingsAccount object"""
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """Calculate the interest amount."""
        return f'{self.interest_rate * self.balance:.2f}'


class CheckingAccount(Account):
    """ Class CheckingAccount for maintaining checking account data.
        CheckingAccount is based on the Account class. Inherits all and attributes.
        Implements additional attribute transaction_fee.
        Overrides deposit and withdraw methods to subtract transaction_fee when calling either of these methods.
    """

    def __init__(self, name, balance, transaction_fee):
        """Initialize a SavingsAccount object"""
        super().__init__(name, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        """Define the withdraw methods by overriding this method from base class."""
        super().withdraw(amount)
        self.balance -= self.transaction_fee

    def deposit(self, amount):
        """Define the withdraw methods by overriding this method from base class."""
        super().deposit(amount)
        self.balance -= self.transaction_fee


# Testing the SavingsAccount class
# Create an object of class SavingsAccount
s1 = SavingsAccount('Maria', Decimal('100.00'), Decimal('0.12'))
# Display the interest rate
print(f'The interest rate should be 0.12: {s1.interest_rate}')
# Call the calculate_interest method
print(f'Calling calculate_interest method should return 12.00: {s1.calculate_interest()}')

# Testing the CheckingAccount class
# Create an object of class CheckingAccount
c1 = CheckingAccount('Paul', Decimal(100.00), Decimal('1.15'))
# Display the transaction fee
print(f'THe transaction fee should be 1.15: {c1.transaction_fee}')
# Depositing 100 to the account
c1.deposit(Decimal('100.00'))
# Print the updated balance after depositing: 100 + 100 - 1.15 = 198.85
print(f'The balance after depositing 100 should become 198.85: {c1.balance}')
# Trying to withdraw 300
try:
    c1.withdraw(Decimal('300'))
except ValueError:
    print(f'After failed withdraw attempt the balance is unchanged 198.85: {c1.balance}')
# Current implementation of withdraw leaves place for bug when withdrawing full balance amount.
c1.withdraw(Decimal('198.85'))
print(f'Withdrawing exactly 198.85 worked, fee was charged from 0 balance, it became negative -1.15: {c1.balance}')
