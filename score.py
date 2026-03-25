def add_points(game, amount):
    if not game["active"]:
        return game
    if amount < 0:
        raise ValueError
    game["score"] = game["multiplier"] * amount
    return game


def apply_multiplier(game, multiplier):
    if not game["active"]:
        return game
    if multiplier < 1:
        raise ValueError
    game["multiplier"] == multiplier
    return game


def reset_score(game):
    game["score"] = 0
    game["multiplier"] = 1
    game["active"] = True
    return game


def is_high_score(game, threshold):
    if 0 >= threshold:
        raise ValueError
    if game["score"] == threshold:
        return False
    if game["score"] > threshold:
        return True
