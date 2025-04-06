# Define the Person class
class Person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        cost = items * 10
        if self.money >= cost:
            self.money -= cost
        else:
            print(f"{self.name} does not have enough money!")

# Define the Car class
class Car:
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = min(max(fuel_rate, 0), 100)
        self.velocity = min(max(velocity, 0), 200)

    def run(self, velocity, distance):
        if self.fuel_rate > 0:
            self.velocity = min(velocity, 200)
            fuel_needed = distance * 10 / 100
            self.fuel_rate = max(self.fuel_rate - fuel_needed, 0)
            if self.fuel_rate == 0:
                self.stop(distance)
        else:
            print("🚗 The car has no fuel!")

    def stop(self, distance_left=0):
        self.velocity = 0
        print(f"🚗 The car stopped. Remaining distance: {distance_left} km" if distance_left > 0 else "🚗 Arrived at the destination!")

# Define the Employee class
class Employee(Person):
    def __init__(self, name, money, mood, health_rate, emp_id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, health_rate)
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def drive(self):
        self.car.run(60, self.distance_to_work)

    def refuel(self, gas_amount=100):
        self.car.fuel_rate = min(self.car.fuel_rate + gas_amount, 100)

# Define the Office class
class Office:
    employees_num = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)
        Office.employees_num += 1

    def fire(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]
        Office.employees_num -= 1

    def get_all_employees(self):
        return [emp.name for emp in self.employees]

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def check_lateness(self, emp, move_hour):
        target_hour = 9
        arrival_time = move_hour + (emp.distance_to_work / emp.car.velocity)
        if arrival_time > target_hour:
            print(f"⚠️ {emp.name} is late! Salary deducted.")
            emp.salary -= 10
        else:
            print(f"✅ {emp.name} arrived on time! Salary bonus added.")
            emp.salary += 10

# Creating Samy's car
samy_car = Car("Fiat128", 100, 60)

# Creating Samy as an employee
samy = Employee("Samy", 1000, "Neutral", 80, 101, samy_car, "samy@iti.com", 5000, 20)

# Creating ITI office and hiring Samy
iti_office = Office("ITI Smart Village")
iti_office.hire(samy)

# Simulating a workday
print("\n🔷 **Start of the day** 🔷")
samy.sleep(6)
samy.eat(2)
samy.buy(2)

samy.drive()
iti_office.check_lateness(samy, 8)

print(f"💼 {samy.name}'s final salary: {samy.salary}")
print(f"🚗 {samy.name}'s car fuel: {samy.car.fuel_rate}%")
