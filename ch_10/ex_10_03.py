# Exercise 10_03 from Deitel: Intro to Python and CS

""" Modify Section 10.4.2’s Time class to provide a readonly property universal_str
that returns a string representation of a Time in 24-hour clock format
with two digits each for the hour, minute and second, as in '22:30:00' (for 10:30 PM) or '06:30:00' (for 6:30 AM).
Test your new read-only property. """

# Solution at the very end of the class definition


class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self.hour = hour  # 0-23
        self.minute = minute  # 0-59
        self.second = second  # 0-59

    @property
    def hour(self):
        """Return the hour."""
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Set the hour."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._hour = hour

    @property
    def minute(self):
        """Return the minute."""
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Set the minute."""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')

        self._minute = minute

    @property
    def second(self):
        """Return the second."""
        return self._second

    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._second = second

    def set_time(self, hour=0, minute=0, second=0):
        """Set values of hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, ' +
                f'second={self.second})')

    def __str__(self):
        """Return Time string in 12-hour clock format."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM'))

    @property
    def time(self):
        return self._hour, self._minute, self._second

    @time.setter
    def time(self, time_tuple):
        self.set_time(time_tuple[0], time_tuple[1], time_tuple[2])

    # SOLUTION
    @property
    def universal_str(self):
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'


my_time = Time(6, 7, 14)
print(my_time.universal_str)
