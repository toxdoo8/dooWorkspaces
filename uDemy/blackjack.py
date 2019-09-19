import random

class Card(object):
  def __init__(self):
    pass

  def __str__(self):
    pass

class Deck(object):
  def __init__(self):
    self.deck = [] # start with an empty list
    for suit in suites:
      for rank in ranks:
        pass

  def __str__(self):
    pass

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    pass

class Hand(object):
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0

  def __str__(self):
    pass

  def func(self):