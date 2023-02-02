print("hello")


class Person:
    def __init__(self, name, money, mood, healthrate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthrate = healthrate

    def sleep(self, shours):
        if shours > 7:
            print("lazy")
        elif shours == 7:
            print("happy")
        else:
            print("tired")

    def eat(self, no_of_meals):
        if no_of_meals == 1:
            print("50%")
        elif no_of_meals == 2:
            print("75%")
        if no_of_meals == 3:
            print("100%")

    def buy(self, no_of_items):
        for i in range(no_of_items):
            self.money -= 10


# ahmed = Person("ahmed", 100, "smile", "grate")
# ahmed.sleep(5)
# ahmed.buy(3)
# ahmed.buy(1)

#print(ahmed.money)


class Employee(Person):
    def __init__(self, name, money, mood, healthrate, id, car, email, salary, distanceToWork):
        super(Employee, self).__init__(name, money, mood, healthrate)
        self.id = id
        self.car = car
        self.email = email
        self.__salary = salary
        self.distanceToWork = distanceToWork
    @property
    def Salary(self):
        return self.__salary
    @Salary.setter
    def Salary(self,newsalary):
        if newsalary < 1000:
            print("invalid salary please review it")
        else:
            self.__salary = newsalary

    def work(self, whours):
        if whours > 8:
            print("tired")
        elif whours == 8:
            print("happy")
        else:
            print("lazy")

    def drive(self,distance):
        Car.run(velocity,distance)
        pass

    def refuel(self,gasAmount):
        Car.fuelRate = self.gasAmount


    def send_mail(self):
        pass


ostaz_ahmed = Employee("ostaz ahmed", 100, "smile", "grate", 2, "logan", "a@a.a", 4000, 20)
ostaz_ahmed.work(8)
print(ostaz_ahmed.name)
ostaz_ahmed.name = "elostaz ahmed"
print(ostaz_ahmed.name)
print(ostaz_ahmed.Salary)
ostaz_ahmed.Salary = 1000
print(ostaz_ahmed.Salary)
ostaz_ahmed.Salary = 100
print(ostaz_ahmed.Salary)



class Office:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        pass

    def get_employee(self):
        pass

    def fire(self):
        pass

    def hire(self):
        pass

    def calculate_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self,velocity,distance):
        no_of_10_km = int(self.distance / 10)
        for i in range (no_of_10_km):
            self.fuelRate = int(self.fuelRate-(self.fuelRate * 0.1))
            self.distance -= 10
            if self.fuelRate == 0:
                stop(self.Distance)
        self.velocity = velocity


    def stop(self,Distance):
        self.velocity = 0
        if Distance == 0:
            print ("you arrived")
        else:
            print("the remaining distance is "+Distance)

