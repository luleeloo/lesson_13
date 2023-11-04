class Academy:
    __name = "So skilled!"
    __city = "Kharkiv"

    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 6:
            self.__name = name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if len(city) > 6:
            self.__city = city

    def show_info(self):
        print(f"Name: {self.name}, City: {self.city}")


class Building(Academy):
    __name = "own"
    __city = "Kharkiv"
    __building_no = "own"

    def __init__(self, name, city, building_no):
        super().__init__(name, city)
        self.building_no = building_no
        self.classrooms = []

    def show_info(self):
        print(f"Name: {self.name}, City: {self.city}, Building number: {self.building_no}")

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)


class Classroom(Building):
    def __init__(self, name, city, building_no, classroom_no):
        super().__init__(name, city, building_no)
        self.classroom_no = classroom_no

class Person:
    def __init__(self, name, age, city, id_number):
        self.name = name
        self.city = city
        self.age = age
        self._ID_number = id_number


class Student(Person):
    def __init__(self, name, age, city, id_number, year, group):
        super().__init__(name,age, city, id_number)
        self.year = year
        self.group = group

    def show_group(self):
        print(f"This student studies in the {self.group}")


build3 = Building("Old building", "Kharkiv", "3")
build3.show_info()
Ann = Student("Anna Kharkivska", "19", "Kharkiv", "12678", "1", "12AE")
Ann.show_group()


