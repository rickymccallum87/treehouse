class Mage:
  mana = 10

  def fireball(self, enemy):
    if self.mana > 0:
      self.mana -= 1
      if enemy.inCombat:
        enemy.health -= 3
        print('ka-boom!')
        if enemy.health < 1:
          enemy.inCombat = False
          print('x.x')
      else:
        print('whiff!')
    else:
      print('not enough mana')
    return self.mana

class Enemy:
  health = 10
  inCombat = True

  def run(self):
    self.inCombat = False
    print('eeek!')
