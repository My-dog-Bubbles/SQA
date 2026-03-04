import pytest
from score import *

def test_add_point_negative_point(game):
    with pytest.raises(valueError):
        add_points(game,-10)
        assert result["score"] == 0

def test_add_points_inactive_game1(game2):
    result = add_points(game,10)
    assert result["score"] == 0
def test_add_points_inactive_game2(game):
    game["active"] = False
    result = add_points(game,10)
    assert result["score"] == 0

def test_add_multiplier(game):
    with pytest.raises(valueError):
        add_multiplier(game,0)
        assert result["multiplier"] == 1

def test_add_multiplier_inactive_game1(game2):
    result = add_multiplier(game,10)
    assert result["multiplier"] == 0
def test_add_multiplier_inactive_game2(game):
    game["active"] = False
    result = add_multiplier(game,10)
    assert result["multiplier"] == 0

def test_reset_score_reset_game_to_default(game):
    change1 = add_multiplier(game,10)
    change2 = add_points(game,10)
    result = reset_score(game)
    assert result["score"] == 0 and result["multiplier"]

def test_reset_score_inactive_game(game):
    result = reset_score(game)
    assert result["score"] == 0 and result["multiplier"]
def test_add_multiplier_inactive_game2(game):
    game["active"] = False
    result = reset_score(game)
    assert result["score"] == 0 and result["multiplier"]

def is_high_score_threshold_equal_score(game):
    