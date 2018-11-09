class Employee:
    
    raise_amount = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay        
        self.email = first +'.'+ last +'@mail.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.6

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

dev1 = Developer('Sagar', 'Handore', 200, 'Java')
dev2 = Developer('Apurv', 'Kolapkar', 150, 'Docker')

print(dev1.email)
print(dev1.prog_lang)

print(dev2.email)
print(dev2.prog_lang)


# print('Old: ',dev1.pay)
# dev1.apply_raise()
# print('New: ',dev1.pay)
