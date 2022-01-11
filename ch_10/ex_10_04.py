# Exercise 10_04 from Deitel: Intro to Python and CS

""" Section 10.4.2’s Time class represents the time as three integer values.
Modify the class to store the time as the total number of seconds since midnight.
Replace the _hour, _minute and _second attributes with one _total_seconds attribute.
Modify the bodies of the hour, minute and second properties’ methods to get and set _total_seconds.
Use the modified Time class to show that the updated class Time is interchangeable with the original one. """


class Time:
    """Class Time with read-write properties."""

    def __init__(self, total_seconds):
        """Initialize each attribute."""
        self._total_seconds = total_seconds

    @property
    def hour(self):
        """Return the hour."""
        return self._total_seconds // 3600

    @hour.setter
    def hour(self, hour):
        """Set the hour."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._total_seconds -= self._total_seconds // 3600 * 3600
        self._total_seconds += hour * 3600

    @property
    def minute(self):
        """Return the minute."""
        return self._total_seconds % 3600 // 60

    @minute.setter
    def minute(self, minute):
        """Set the minute."""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')

        self._total_seconds -= self._total_seconds % 3600 // 60 * 60
        self._total_seconds += minute * 60

    @property
    def second(self):
        """Return the second."""
        return self._total_seconds % 60

    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._total_seconds -= self._total_seconds % 60
        self._total_seconds += second

    def set_time(self, hour=0, minute=0, second=0):
        """Set values of hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        """Return Time string for repr()."""
        return f'Time(hour={self.hour}, minute={self.minute}, second={self.second})'

    def __str__(self):
        """Return Time string in 12-hour clock format."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM'))

    @property
    def time(self):
        return self.hour, self.minute, self.second

    @time.setter
    def time(self, time_tuple):
        self.set_time(time_tuple[0], time_tuple[1], time_tuple[2])

    # SOLUTION
    @property
    def universal_str(self):
        return f'{self.hour:0>2}:{self.minute:0>2}:{self.second:0>2}'


my_time = Time(3940)  # the time should be 01:05:40
print('the time should be 01:05:40')
print(f'{str(my_time.universal_str):.^30}')

# update hours, minutes, seconds - internally we update only the _total_seconds attribute
# the time should be 06:42:17
my_time.hour = 6
my_time.minute = 42
my_time.second = 17
print('the time should be 06:42:17')
print(f'{str(my_time.universal_str):.^30}')

# checking that set_time method correctly uses properties hour, minute and second
my_time.set_time(17, 22, 33)  # the time should be 17:22:33
print('the time should be 17:22:33')
print(f'{str(my_time.universal_str):.^30}')

my_time.time = 23, 0, 1  # the time should be 11:00:01 PM
print('the time should be 11:00:01 PM')
print(f'{str(my_time):.^30}')
