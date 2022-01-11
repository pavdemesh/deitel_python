# trying and playing with setter and getters

class Time:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours_prop = hours
        self.minutes_prop = minutes
        self.seconds_prop = seconds

    @property
    def hours_prop(self):
        return self._actual_hours

    @hours_prop.setter
    def hours_prop(self, la_hour):
        self._actual_hours = la_hour

    def __str__(self):
        return f"hour = {self.hours_prop}, minute = {self.minutes_prop}, seconds = {self.seconds_prop}"


wake = Time(11, 25, 33)

print(wake)

wake.hours_prop = 22
wake.minutes_prop = 11
wake._actual_hours = 3

print(wake)
