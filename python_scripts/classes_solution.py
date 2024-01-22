# Like `def` for functions, `class` is a keyword for classes.
from datetime import date

class TestDog:  # Usually class names are capitalized.
    # The `__init__` method is the constructor.
    # It is called when an instance of the class is created.
    # The first argument is always `self`.
    # `self` refers to the instance of the class.
    def __init__(self, name, owner, sex, dob, color, tricks=None):
        self.name = name
        self._dob = date(dob)
        self.owner = owner
        self._sex = sex
        self._color = color
        if type(dob) is date:
            self._dob = dob
        elif type(dob) is str:
            self._dob = date.fromisoformat(dob)
        else:
            raise TypeError("Date of birth must be date or string.")
            
        if tricks is None:
            # If no tricks supplied, set to empty set.
            self.tricks = set([])
        else:
            if type(tricks) is str:
                # If only one trick supplied, set to set with one element.
                self._tricks = set([tricks])
            elif type(tricks) is list:
                # If list of tricks supplied, set to set of tricks.
                self._tricks = set(tricks)
            elif type(tricks) is set:
                # If set of tricks supplied, set to set of tricks.
                self._tricks = tricks
            else:
                raise TypeError("Tricks must be string, list, or set.")

    @property
    def sex(self):
        return self._sex

    @property
    def color(self):
        return self._color

    @property
    def age(self):
        # use datetime to get age in years
        return (date.today() - self._dob).days // 365

    @property
    def tricks(self):
        return self._tricks

    @tricks.setter
    def tricks(self, tricks):
        if type(tricks) is str:
            # If only one trick supplied, set to set with one element.
            self._tricks.add(tricks)
        elif type(tricks) is list:
            # If list of tricks supplied, set to set of tricks.
            self._tricks.update(set(tricks))
        elif type(tricks) is set:
            # If set of tricks supplied, set to set of tricks.
            self._tricks.update(tricks)
        else:
            raise TypeError("Tricks must be string, list, or set.")
