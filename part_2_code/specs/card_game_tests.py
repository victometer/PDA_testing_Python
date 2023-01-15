import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame (unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame ()
        self.card1 = Card ('hearts', 9)
        self.card2 = Card ('clubs', 1)
        self.cards = [self.card1, self.card2]


    def test_cards_have_an_ace(self):
        self.card_game.check_for_ace(self.card2)
        self.assertEqual(1, self.card2.value)

    def test_for_highest_card(self):
        self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(9, self.card1.value)
    
    def test_cards_total(self):
        total_value = self.card_game.cards_total(self.cards)
        self.assertEqual(10, total_value)






        