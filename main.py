class Player:
  def __init__(self, name, health, attack, defence):
    self.name = name
    self.health = health
    self.attack = attack
    self.defence = defence

  def redo(self, name, health, attack, defence):
    self.health = health
    self.attack = attack
    self.defence = defence
    
  def statCheck():
    if int(self.health) + int(self.attack) + int(self.defence) > 300:
      result = "REDO"
    else:
      result = "CONTINUE"
    return result

player = Player(input("Enter username: "), input("Enter health stat: "), input("Enter attack stat: "), input("Enter defence stat: "))
if player.statCheck() == "REDO":
  print(f"Max stat points is 300, and you added {int(self.health) - int(self.attack) - int(self.defence)} too many, please try agian\n")
  player.redo(input("Enter username: "), input("Enter health stat: "), input("Enter attack stat: "), input("Enter defence stat: "))

print(f"Player name: {player.name}\nPlayer health: {player.health}\nPlayer attack: {player.attack}\nPlayer defence: {player.defence}")
