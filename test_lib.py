from lib import average, get_minimum
from lib import Person, Wizard, HealthPotion, Inventory

def test_average():
    input1 = [11, -11, 10, 20]
    expected_result=7.5
    actual_result = average(input1)
    assert actual_result == expected_result

def test_minimun():
    input1 = [11, -11, 10, 20]
    expected_result= input1[1]
    actual_result = get_minimum(input1)
    assert actual_result == expected_result


# --- Tests pour Person ---

def test_person_initialization():
    p = Person("Arthur")
    assert p.name == "Arthur"
    assert p.life_points == 100

def test_person_hit_reduces_target_life():
    attacker = Person("Arthur")
    target = Person("Merlin")
    
    attacker.hit(target)
    
    assert target.life_points == 90
    assert attacker.life_points == 100 # Vérifie que l'attaquant ne perd pas de vie

def test_person_is_dead():
    p = Person("Arthur")
    assert p.is_dead() is False
    
    p.life_points = 0
    assert p.is_dead() is True
    
    p.life_points = -10
    assert p.is_dead() is True

def test_person_gained_life_points():
    p = Person("Arthur")
    p.gained_life_points(20)
    assert p.life_points == 120

# --- Tests pour Wizard ---

def test_wizard_initialization():
    w = Wizard("Gandalf")
    assert w.name == "Gandalf"
    assert w.life_points == 80

def test_wizard_hit_does_more_damage_and_returns_person():
    w = Wizard("Gandalf")
    target = Person("Orc")
    
    result = w.hit(target)
    
    assert target.life_points == 85
    assert result == target # Le wizard renvoie l'objet frappé, contrairement à Person

# --- Tests pour HealthPotion ---

def test_health_potion_usage():
    p = Person("Arthur")
    potion = HealthPotion()
    
    potion.was_used_by(p)
    
    assert p.life_points == 110

# --- Tests pour Inventory ---

def test_inventory_add_and_get_objects():
    inv = Inventory()
    potion1 = HealthPotion()
    potion2 = HealthPotion()
    
    assert len(inv.get_objects()) == 0
    
    inv.add_object(potion1)
    inv.add_object(potion2)
    
    items = inv.get_objects()
    assert len(items) == 2
    assert items[0] == potion1
    assert items[1] == potion2
# test_average()