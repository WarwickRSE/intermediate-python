# Like `def` for functions, `class` is a keyword for classes.
from datetime import date


class TestDog:  # Usually class names are capitalized.
    # The `__init__` method is the constructor.
    # It is called when an instance of the class is created.
    # The first argument is always `self`.
    # `self` refers to the instance of the class.
    def __init__(self, name, owner, sex, dob, color, tricks=None,
                 date_format="dd/mm/yyyy", breed=None, parents=None):
        self.name = name
        self.owner = owner
        self._sex = sex
        self._color = color
        if type(dob) is date:
            self._dob = dob
        elif type(dob) is str:
            # get position of dd mm and yy or yyyy in date_format
            assert len(date_format) == len(dob), "Date format and date\
                  must be same length."
            dd_pos = date_format.find("dd")
            if dd_pos == -1:
                raise ValueError("Date format must contain 'dd'.")
            mm_pos = date_format.find("mm")
            if mm_pos == -1:
                raise ValueError("Date format must contain 'mm'.")
            yyyy_pos = date_format.find("yyyy")
            if yyyy_pos == -1:
                yy_pos = date_format.find("yy")
                if yy_pos == -1:
                    raise ValueError("Date format must contain 'yyyy' or 'yy'")

            # get date, month, and year from dob
            dd = int(dob[dd_pos:dd_pos+2])
            mm = int(dob[mm_pos:mm_pos+2])
            if yyyy_pos == -1:
                yy = int(dob[yy_pos:yy_pos+2])
                if yy > date.today().year - 2000:
                    yyyy = 1900 + yy
                else:
                    yyyy = 2000 + yy
            else:
                yyyy = int(dob[yyyy_pos:yyyy_pos+4])
            self._dob = date(yyyy, mm, dd)
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

        if breed is None and parents is None:
            assert False, "Breed or parents must be supplied."
        elif breed is not None and parents is not None:
            assert False, "Breed and parents cannot be supplied together."
        elif breed is not None:
            if type(breed) is str:
                self._breed = (breed,)
            elif type(breed) is list:
                self._breed = tuple(breed)
            elif type(breed) is tuple:
                self._breed = breed
        else:
            assert len(parents) == 2, "Exactly two parents must be supplied."
            assert isinstance(parents[0], type(self)), "Parents must be Dog."
            assert isinstance(parents[1], type(self)), "Parents must be Dog."
            assert parents[0]._sex != parents[1]._sex, "Parents must be of opposite sexes."
            # Logic to determine breed from parents.
            self.parents = parents
            if parents[0].breed == parents[1].breed:
                self._breed = (parents[0].breed)
            elif len(parents[0].breed) != len(parents[1].breed):
                if len(parents[0].breed) == 1:
                    self._breed = parents[0].breed + parents[0].breed + parents[1].breed
                elif len(parents[1].breed) == 1:
                    self._breed = parents[0].breed + parents[1].breed + parents[1].breed
                else:
                    self._breed = parents[0].breed + parents[1].breed

                if len(self._breed) > 4:
                    self._breed = ("Mutt",)
            else:
                self._breed = parents[0].breed + parents[1].breed

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

    @property
    def breed(self):
        return self._breed
