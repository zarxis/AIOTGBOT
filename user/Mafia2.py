class Person:
    name = 'Unnamed'

    def GetName(self):
        return self.name

    power = 0

    def GetPower(self):
        return self.power

    position = 0

    def GetPosition(self):
        return self.position

    role = 'Unknown'

    def GetRole(self):
        return self.role

    isInvulnerable = False

    def IsInvul(self):
        return self.isInvulnerable

    isAlive = True

    def IsAlive(self):
        return self.isAlive


class Shanon(Person):
    abilityCounter = 1

    def __init__(self, position, role):
        self.name = 'Shanon'
        self.power = 2
        self.position = position
        self.role = role

    def ability(self, amountOfPayers, listOfPersons):
        if self.abilityCounter > 0:
            if amountOfPayers < 9:
                self.isInvulnerable = True
            else:
                a = 1
            self.abilityCounter -= 1
        else:
            print('Ability is already used')


class Jessica(Person):
    abilityCounter = 1

    def __int__(self, position, role):
        self.name = 'Jessica'
        self.power = 3
        self.position = position
        self.role = role


class Eve(Person):
    abilityCounter = 1

    def __init__(self, position, role):
        self.name = 'Jessica'
        self.power = 3
        self.position = position
        self.role = role


class Rudolf(Person):
    abilityCounter = 1

    def __int__(self, position, role):
        self.name = 'Rudolf'
        self.power = 2
        self.position = position
        self.role = role


class Kirie(Person):
    abilityCounter = 1

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 2
        self.position = position
        self.role = role


class Natsuhi(Person):
    abilityCounter = 1

    def __init__(self, position, role):
        self.name = Natsuhi
        self.power = 2
        self.position = position
        self.role = role


class Kumasava(Person):
    abilityCounter = 1

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 2
        self.position = position
        self.role = role


class Kraus(Person):
    abilityCounter = 1

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 4
        self.position = position
        self.role = role


class Kinzo(Person):
    abilityCounter = 1

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 2
        self.position = position
        self.role = role


class Batler(Person):
    abilityCounter = 1

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 2
        self.position = position
        self.role = role


class Kanon(Person):
    abilityCounter = 1

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 1
        self.position = position
        self.role = role


class Djordj(Person):
    abilityCounter = 1

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 3
        self.position = position
        self.role = role


class Hideoshi(Person):
    abilityCounter = 1

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 2
        self.position = position
        self.role = role


'''
class Goda(Person):
    abilityCounter = 1;

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 2
        self.position = position
        self.role = role;


class Rose(Person):
    abilityCounter = 1;

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 2
        self.position = position
        self.role = role;


class Nandjo(Person):
    abilityCounter = 1;

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 2
        self.position = position
        self.role = role;


class Marie(Person):
    abilityCounter = 1;

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 2
        self.position = position
        self.role = role;

class Genji(Person):
    abilityCounter = 1;

    def __int__(self, position, role):
        self.name = 'Kirie'
        self.power = 2
        self.position = position
        self.role = role
'''
