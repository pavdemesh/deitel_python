# Exercise 10_05 from Deitel: Intro to Python and CS

"""
With duck typing, objects of unrelated classes can respond to the same method calls if they implement those methods.
In Section 10.8, you created a list containing a CommissionEmployee and a SalariedCommissionEmployee.
Then, you iterated through it, displaying each employee’s string representation and earnings.
Create a class SalariedEmployee for an employee that gets paid a fixed weekly salary.
Do not inherit from CommissionEmployee or SalariedCommissionEmployee.
In class SalariedEmployee, override method __repr__ and provide an earnings method.
Demonstrate duck typing by creating an object of your class, adding it to the list at the end of Section 10.8.
Then execute the loop to show that it properly processes objects of all three classes.
"""

from decimal import Decimal


class CommissionEmployee:
    """An employee who gets paid commission based on gross sales."""

    def __init__(self, first_name, last_name, ssn,
                 gross_sales, commission_rate):
        """Initialize CommissionEmployee's attributes."""
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales  # validate via property
        self.commission_rate = commission_rate  # validate via property

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sales(self):
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, sales):
        """Set gross sales or raise ValueError if invalid."""
        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= to 0')

        self._gross_sales = sales

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, rate):
        """Set commission rate or raise ValueError if invalid."""
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError(
                'Interest rate must be greater than 0 and less than 1')

        self._commission_rate = rate

    def earnings(self):
        """Calculate earnings."""
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        """Return string representation for repr()."""
        return ('CommissionEmployee: ' +
                f'{self.first_name} {self.last_name}\n' +
                f'social security number: {self.ssn}\n' +
                f'gross sales: {self.gross_sales:.2f}\n' +
                f'commission rate: {self.commission_rate:.2f}')


class SalariedCommissionEmployee(CommissionEmployee):
    """An employee who gets paid a salary plus
    commission based on gross sales."""

    def __init__(self, first_name, last_name, ssn,
                 gross_sales, commission_rate, base_salary):
        """Initialize SalariedCommissionEmployee's attributes."""
        super().__init__(first_name, last_name, ssn,
                         gross_sales, commission_rate)
        self.base_salary = base_salary  # validate via property

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, salary):
        """Set base salary or raise ValueError if invalid."""
        if salary < Decimal('0.00'):
            raise ValueError('Base salary must be >= to 0')

        self._base_salary = salary

    def earnings(self):
        """Calculate earnings."""
        return super().earnings() + self.base_salary

    def __repr__(self):
        """Return string representation for repr()."""
        return ('Salaried' + super().__repr__() +
                f'\nbase salary: {self.base_salary:.2f}')


class SalariedEmployee:
    """Class representing an employee who gets paid a weekly salary."""

    def __init__(self, first_name, last_name, ssn, weekly_salary):
        """Initialize SalariedEmployee attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.weekly_salary = weekly_salary

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, salary):
        """Set weekly_salary or raise ValueError if invalid."""
        if salary < Decimal('0.0'):
            raise ValueError('salary worked must be >= 0.0')

        self._weekly_salary = salary

    def earnings(self):
        """Calculate earnings."""
        return self.weekly_salary

    def __repr__(self):
        """Return string representation for repr()."""
        return ('SalariedEmployee: ' +
                f'{self.first_name} {self.last_name}\n' +
                f'social security number: {self.ssn}\n' +
                f'weekly salary: {self.weekly_salary:.2f}')


# Define 3 employees - one for each class
emp1 = CommissionEmployee('Sue', 'Jones', '333-33-3333', Decimal('10000.00'), Decimal('0.06'))
emp2 = SalariedCommissionEmployee('Bob', 'Lewis', '444-44-444', Decimal('15000.00'), Decimal('0.07'), Decimal('300.00'))
emp3 = SalariedEmployee('John', 'Snow', '777-8888-999', Decimal('2_350.05'))

# Add employees to a list
employees = [emp1, emp2, emp3]

# Iterate over list and print each employee and their respective earnings
for employee in employees:
    print(employee)
    print(f'total earnings are: {employee.earnings():,.2f}\n')
