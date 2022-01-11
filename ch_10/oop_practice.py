class Amy:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def mira(self):
        return

    @mira.setter
    def mira(self, ttuple):
        self._name = ttuple[0]


waka = Amy("Jane", 33)
print(waka._name)
waka.mira = 'jana', 98, 5
print(waka._name)
