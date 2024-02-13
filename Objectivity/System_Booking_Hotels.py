class Room:
    def __init__(self,number, type, availibilty, price):
        self.number= number
        self._type= type
        self.availibility= availibilty
        self.price= price

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, new_type):
        valid_types = ["Apartament", "Superior", "SuperiorPlus"]
        if new_type in valid_types:
            self._type = new_type
        else:
            print("Nieprawidłowy typ pokoju. Dostępne typy to: apartament, Superior, SuperiorPlus")

class Reservation:
    def __init__(self, ):