class Player:
  def __init__(self, name, health, attack, defence):
    self.name = name
    self.health = health
    self.attack = attack
    self.defence = defence

  def change(self, health, attack, defence):
    self.health = health
    self.attack = attack
    self.defence = defence
    
print("You have a max of 300 stat points to use total\n")
player = Player(input("Enter username: "), input("Enter health stat: "), input("Enter attack stat: "), input("Enter defence stat: "))
print(f"Player name: {player.name}\nPlayer health: {player.health}\nPlayer attack: {player.attack}\nPlayer defence: {player.defence}")
if int(player.health) + int(player.attack) + int(player.defence) > 300:
  print(f"Max stat points is 300, and you added {abs(int(player.health) + int(player.attack) + int(player.defence)) - 300} too many, please try agian\n")
  player.change(input("Enter health stat: "), input("Enter attack stat: "), input("Enter defence stat: "))
print(f"Player name: {player.name}\nPlayer health: {player.health}\nPlayer attack: {player.attack}\nPlayer defence: {player.defence}")
