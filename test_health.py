import pytest
from health import *

def test_take_damage(player):
    result = take_damage(player, 30)
    assert result["health"] == 70

def test_heal_increases_health(player):
    result = heal(player, 30)
    assert result["health"] == 100

def test_is_alive_returns_true_when_healthy(player):
    assert is_alive(player) == True