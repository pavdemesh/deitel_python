# trying and playing with setter and getters

class Time:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours_prop(self):
        return self._hours

    def __str__(self):
        return f"hour = {self.hours_prop}, minute = {self.minutes}, seconds = {self.seconds}"


wake = Time(11, 25, 33)

print(wake)

print(wake.hours_prop)
print(wake._hours)
