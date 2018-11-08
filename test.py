class Employee:
    
    raise_amount = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay        
        self.email = first +'.'+ last +'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Piyush', 'Ghate', 200)
emp2 = Employee('Vikas', 'Chauhan', 150)

# print(emp1)
# print(emp2)


# emp1.first = 'Piyush'
# emp1.last = 'Ghate'
# emp1.email = 'test1@gmail.com'
# emp1.pay = '200'

# emp2.first = 'Vikas'
# emp2.last = 'Chauhan'
# emp2.email = 'test2@gmail.com'
# emp2.pay = '250'

print(emp1.email)
print(emp2.email)


# print('{} {}'.format(emp1.first, emp1.last)) #output: Piyush Ghate

# print(emp1.fullname())
# print(Employee.fullname(emp1))
# print(emp2.fullname())

print('old pay: ',emp1.pay)
print('Hike by: ',Employee.raise_amount)
emp1.apply_raise()
print('new pay: ',emp1.pay)