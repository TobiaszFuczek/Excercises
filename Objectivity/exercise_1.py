class Person:
    def __init__(self, imie, nazwisko, wiek):
        self.imie= imie
        self.nazwisko= nazwisko
        self.wiek= wiek

    def show_all_data(self):
        return(f"Osoba: {self.imie}, {self.nazwisko}, {self.wiek}")

    def show_full_name(self):
        return(f"Imie i Nazwisko Osoby: {self.imie}, {self.nazwisko}")

    def one_year_add(self):
        self.wiek += 1

person_1= Person("Robert", "Lewandowski", 35)
print(person_1.show_all_data())
print(person_1.show_full_name())
person_1.one_year_add()
print(f"Wiek zwiekszony o 1 rok: {person_1.wiek}")


