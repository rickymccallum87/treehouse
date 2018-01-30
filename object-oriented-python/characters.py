class Mage:
  mana = 10

  def fireball(self):
    if self.mana > 0:
      self.mana -= 1
      print('ka-boom!')
    else:
      print('not enough mana')
    return self.mana
