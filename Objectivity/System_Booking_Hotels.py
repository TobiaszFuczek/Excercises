class Room:
    def __init__(self,number, type, availability, price):
        self.number= number
        self._type= type
        self.availability= availability
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
    def __init__(self):
        self.available_rooms= []
        self.unavailable_rooms= []

    def check_availability_room(self, number):
        if number in [room.number for room in self.available_rooms]:
            print(f"Pokój {number} jest dostępny.")
        elif number in [room.number for room in self.unavailable_rooms]:
            print(f"Pokój {number} jest niedostępny.")
        else:
            print(f"Pokój {number} nie istnieje.")

    def reserve_room(self, number):
        room = self.find_room_by_number(number)
        if room:
            if room.availability:
                self.available_rooms.remove(room)
                self.unavailable_rooms.append(room)
                room.availability = False
                print(f"Pokój {number} został zarezerwowany.")
            else:
                print(f"Pokój {number} jest już zarezerwowany.")
        else:
            print(f"Pokój {number} nie istnieje.")

    def cancel_reservation_room(self, number):
        room = self.find_room_by_number(number)
        if room:
            if room in self.unavailable_rooms:
                self.unavailable_rooms.remove(room)
                self.available_rooms.append(room)
                room.availability = True
                print(f"Rezerwacja pokoju {number} została anulowana.")
            else:
                print(f"Pokój {number} nie jest zarezerwowany.")
        else:
            print(f"Pokój {number} nie istnieje.")

    def find_room_by_number(self, number):
        for room in self.available_rooms + self.unavailable_rooms:
            if room.number == number:
                return room
        return None


# Przykładowe użycie:
room1 = Room(101, "Apartament", True, 200)
room2 = Room(102, "Superior", False, 150)

reservation = Reservation()
reservation.available_rooms = [room1, room2]
reservation.unavailable_rooms = []

reservation.check_availability_room(room1.number)
reservation.check_availability_room(room2.number)

reservation.reserve_room(room1.number)
reservation.reserve_room(room2.number)

reservation.check_availability_room(room1.number)
reservation.check_availability_room(room2.number)

reservation.cancel_reservation_room(room1.number)
reservation.check_availability_room(room1.number)