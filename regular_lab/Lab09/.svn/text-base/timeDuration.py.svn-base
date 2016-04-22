import re

class TimeSpan:
    def __init__(self, weeks, days, hours):
        self.weeks = weeks
        self.days = days
        self.hours = hours
        if (type(self.weeks) is not int) or (type(self.days) is not int) or (type(self.hours) is not int):
            raise TypeError("Only accept integer")
        if (self.weeks < 0) or (self.days < 0) or (self.hours < 0):
            raise ValueError("Values could not be negative")
        self.days += int(self.hours / 24)
        self.weeks += int(self.days / 7 )
        self.days %= 7
        self.hours %= 24

    def __str__(self):
        self.weeks = str(self.weeks)
        self.days = str(self.days)
        self.hours = str(self.hours)
        if int(self.weeks) < 10:
            self.weeks = '0' + self.weeks
        if int(self.hours) < 10:
            self.hours = '0' + self.hours
        return self.weeks + 'W ' + self.days + 'D ' + self.hours + 'H'


    def getTotalHours(self):
        return self.weeks * (7*24) + self.days * 24 + self.hours

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return TimeSpan(self.weeks + other.weeks, self.days + other.days, self.hours+ other.hours)
        else:
            raise TypeError("A TimeSpan instance is expected")

    def __mul__(self, other):
        if other == 0:
            raise ValueError("The demoninator could not be zero")
        if isinstance(other, int):
            return TimeSpan(self.weeks * other, self.days * other, self.hours * other)
        else:
            raise TypeError("A integer is expected")

    def __rmul__(self, other):
        if other == 0:
            raise  ValueError("The demoninator could not be zero")
        if isinstance(other, int):
            return TimeSpan(self.weeks * other, self.days * other, self.hours * other)
        else:
            raise TypeError("A integer is expected")