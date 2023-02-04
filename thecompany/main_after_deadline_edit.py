print("hello")


class Person:
    moods = ('happy', 'tired', 'lazy')
    def __init__(self, name ):
        self.name = name
        self.money = 0
        self.mood = "undeclared"
        self.__healthrate = 100

    def sleep(self, shours):
        if shours > 7:
            print(mood[3])
        elif shours == 7:
            print(mood[1])
        else:
            print(mood[2])

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


    @property
    def HealthRate(self):
        return self.__healthRate

    @HealthRate.setter
    def HealthRate(self, newValue):
        if (newValue > 0 and newValue <= 100):
            self.__healthRate = newValue
        else:
            print("healthRate must be between 0 to 100")


ahmed = Person("ahmed")
print(ahmed.name)
print(ahmed.money)
ahmed.money = 80
print(ahmed.money)

#omar = Person("omar", 100, "happy", 50)
# ahmed.sleep(5)
# ahmed.buy(3)
# ahmed.buy(1)

#print(ahmed.money)


class Employee(Person):
    #elst = []
    #dicto = {}
    def __init__(self, name, id, car, email, distanceToWork):
        super(Employee, self).__init__(name)
        self.id = id
        self.car = car
        self.email = email
        self.__salary = 1000
        self.distanceToWork = distanceToWork

        #Employee.elst.append([self.id,self.name,self.__salary])
        #dict[id] = self.name
    @property
    def Salary(self):
        return self.__salary
    @Salary.setter
    def Salary(self,newsalary):
        if newsalary < 1000:
            print("invalid salary please review it")
        else:
            self.__salary = newsalary
    @property
    def Email(self):
        return self.email

    @Email.setter
    def Email(self, email):
        if email.endswith(".com"):
            self.email = email
        else:
            raise ValueError("Invalid email")



    def work(self, whours):
        if whours > 8:
            print("tired")
        elif whours == 8:
            print("happy")
        else:
            print("lazy")

    def drive(self, distance):
        self.car.run(distance, self.car.velocity)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = gasAmount


    @staticmethod
    def send_email(sender, subject, msg, receiver):
        print("email to: "+ receiver+","+ " msg ", msg)



ostaz_ahmed = Employee("ostaz ahmed", 1, "logan", "a@a.com", 20)
print(ostaz_ahmed.id)



# ostaz_omar = Employee("ostaz omar", 100, "smile", "grate", 2, "fiat", "a@a.com", 7000, 20)
# ostaz_ahmed.work(8)
# print(ostaz_ahmed.name)
# ostaz_ahmed.name = "elostaz ahmed"
# print(ostaz_ahmed.name)
# print(ostaz_ahmed.Salary)
# print("s2")
# ostaz_ahmed.Salary = 7000
# print(ostaz_ahmed.Salary)
# ostaz_ahmed.Salary = 100
# print(ostaz_ahmed.Salary)
# print(Employee.elst)
# print("new")




class Office:
    employeesNum = 0
    def __init__(self, name):
        self.name = name
        self.employees = []


    def get_employee(self, empId):
        for empl in self.employees:
            if (empl.id == empId):
                return empl

    def fire(self, empId):
        for em in self.employees:
            if (em.id == empId):
                self.employees.remove(em)
    def hire(self, empl):
        self.employees.append(empl)

    def check_lateness(self,empID,moveHour):
        pass

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time_needed = distance / velocity
        arriving_hour = moveHour + time_needed
        if arriving_hour > targetHour:
            return True
        else:
            return False

    def deduct(self, empId, deduction):
        for em in self.employees:
            if (em.id == empId):
                em.Salary -= deduction
                break

    def reward(self, empId, reward):
        for em in self.employees:
            if (em.id == empId):
                em.Salary += reward
                break

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

class Car:
    velocity = 20
    def __init__(self, name):
        self.name = name
        self.__velocity = 0
        self.__fuelRate = 100


    def run(self,velocity,distance):
        no_of_10_km = int(distance / 10)
        for i in range (no_of_10_km):
            #Car.fuelRate = int(Car.fuelRate-(Car.fuelRate * 0.1))
            self.fuelRate = int(self.fuelRate-(10))
            distance -= 10
            if distance == 0:
                self.stop(distance)
                break
            #print(distance)
            if self.fuelRate == 0:
                self.stop(distance)
                break
        self.velocity = velocity


    def stop(self,distance):
        self.velocity = 0
        if distance == 0:
            print ("you arrived")
        else:
            print("you don't have enought fuel,the remaining distance is "+str(distance))
car1 = Car("fiat punto")
ostaz_ali = Employee("ostaz ali", 1, car1, "a@a.com", 20)
print(ostaz_ali.car.name)
# ostaz_ahmed.refuel(100)
# print(Car.fuelRate)
#
# Car.run(82,20)
# #print(Car.fuelRate)
# print(Car.velocity)
# #print(Car.distance)
# #print(Car.velocity)
# #Car.stop(0)
#
# Office.get_all_employees()
# Office.get_employee(2)
# Office.fire(1)
# Office.get_all_employees()
# print(ostaz_ahmed.Salary)
# Office.deduct(2,1000)
# Office.get_all_employees()
# Office.reward(2,200)
# Office.get_all_employees()