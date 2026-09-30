    


def average(l:list):
    count = 0
    for value in l:
        count+= value
    return count /  len(l)
        

def get_minimum(values:list):
    min = values[0]
    for value in values:
        if value < min:
            min = value
    return min

class Person:
    def __init__(self, name):
        self.name = name
        self.life_points = 100
        
    def hit(self, person):
        person.life_points -= 10
        
    def is_dead(self):
        if self.life_points > 0:
            return False
        return True
        
    def gained_life_points(self, amount):
        self.life_points += amount

class Wizard(Person):
    def __init__(self, name):
        super().__init__(name)
        self.life_points = 80

    def hit(self, person):
        person.life_points -= 15
        return person

class HealthPotion:
    def was_used_by(self, person):
        person.gained_life_points(10)
        
class Inventory:
    def __init__(self):
        self.items = []
        
    def add_object(self, item):
        self.items.append(item)
        
    def get_objects(self):
        return self.items