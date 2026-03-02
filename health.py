def take_damage(player, amount):
    return player - amount

def heal(player,amount):
    return player + amount

def is_alive(player):
    return player > 0