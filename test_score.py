import pytest
from score import *

def test_add_point_negative_point(game):
    with pytest.raises(ValueError):
        result = add_points(game,-10)
        assert result["score"] == 0

def test_add_points_inactive_game(game):
    game["active"] = False
    result = add_points(game,10)
    assert result["score"] == 0

def test_apply_multiplier(game):
    with pytest.raises(ValueError):
        result = apply_multiplier(game,0)
        assert result["multiplier"] == 1

def test_apply_multiplier_inactive_game(game):
    game["active"] = False
    result = apply_multiplier(game,10)
    assert result["multiplier"] == 1

def test_reset_score_reset_game_to_default(game):
    change1 = apply_multiplier(game,10)
    change2 = add_points(game,10)
    result = reset_score(game)
    assert result["score"] == 0 and result["multiplier"] == 1

def test_add_multiplier_inactive_game(game):
    game["active"] = False
    result = reset_score(game)
    assert result["score"] == 0 and result["multiplier"]

def test_is_high_score_threshold_equal_score(game):
    result = is_high_score(game,0)
    assert result == False

def test_is_high_score_raise_ValueError(game):
    with pytest.raises(ValueError):
        result = is_high_score(game,0)
        assert result == 1  