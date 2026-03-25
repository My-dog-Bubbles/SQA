from health import take_damage, heal, is_alive


def test_take_damage_reduces_health(player):
    result = take_damage(player, 30)
    assert result["health"] == 70


def test_take_damage_cannot_go_below_zero(player):
    result = take_damage(player, 999)
    assert result["health"] == 0


def test_take_damage_kills_player_at_zero(player):
    result = take_damage(player, 100)
    assert not result["alive"]


def test_take_damage_by_zero(player):
    result = take_damage(player, 0)
    assert result["health"] == 100
    assert result["alive"]  # This was true


def test_heal_increases_health(player):
    player["health"] = 60
    result = heal(player, 20)
    assert result["health"] == 80


def test_heal_cannot_exceed_max_health(player):
    player["health"] = 90
    result = heal(player, 50)
    assert result["health"] == 100


def test_heal_does_nothing_when_dead(player):
    player["health"] = 0
    player["alive"] = False
    result = heal(player, 50)
    assert result["health"] == 0
    assert not result["alive"]


def test_is_alive_returns_true_when_healthy(player):
    assert is_alive(player)


def test_is_alive_returns_false_when_dead(player):
    player["health"] = 0
    player["alive"] = False
    assert not is_alive(player)


def test_is_alive_returns_false_at_zero_health(player):
    player["health"] = 0
    player["alive"] = False
    assert not is_alive(player)
