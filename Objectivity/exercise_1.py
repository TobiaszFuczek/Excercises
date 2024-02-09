class Person:
    def __init__(self, imie, nazwisko, wiek):
        self.imie= imie
        self.nazwisko= nazwisko
        self.wiek= wiek

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, value):
        if type(value) == str:
            self._imie = value

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, value):
        if type(value) == str:
            self._nazwisko = value

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, value):
        if type(value) == int and value >= 0:
            self._wiek = value
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


class Student(Person):
    def __init__(self,imie, nazwisko, wiek, index_id):
        super().__init__(imie,nazwisko,wiek)
        self.index_id= index_id

    def show_all_information(self):
        print(f"Informacje o Studencie: {self.imie}, {self.nazwisko}, {self.wiek}, {self.index_id}")

    def index_Student(self):
        print(f"Index Studenta: {self.index_id}")

    def __str__(self):
        return f"{self.index_id} : {self.nazwisko}"

student_1= Student("Piotr", "Zielinski", 33, 5543)
student_1.show_all_information()
student_1.index_Student()
print(student_1)

class Course:
    def __init__(self):
        self.participants = []
    def add_to_course(self, participant):
        self.participants.append(participant)
    def __str__(self):
        return print(person_1.show_full_name())

course= Course()

course.add_to_course(person_1)
course.add_to_course(student_1)
print(course)
