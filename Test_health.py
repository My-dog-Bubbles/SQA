from health import *

def test_take_damage_reduce_health():
    assert take_damage(100,33) == 67

def test_heal_adds_health():
    assert heal(67,33) == 100

def test_is_alive_ture():
    assert is_alive(100) == True