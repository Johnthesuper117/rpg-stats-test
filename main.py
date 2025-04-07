class Player:
  def __init__(self, name, health, attack, defence):
    self.name = name
    self.health = health
    self.attack = attack
    self.defence = defence

player = Player(input("Enter username: "), input("Enter health stat: "), input("Enter attack stat: "), input("Enter defence stat: "))
print(f"Player name: {player.name}\nPlayer health: {player.health}\nPlayer attack: {player.attack}\nPlayer defence: {player.defence}")
