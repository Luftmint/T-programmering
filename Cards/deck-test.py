
# Skapa en kortlek med hjälp av objektorienterad programmering - använd klasser
# Tips: du kan använda symboler för kortfärger: suits = ["♠", "♥", "♣", "♦"]

import os


class Card:                    # Class  
    def __init__(self, suit, value):           # Dundermetod / specialmetod
        self.suit = suit                       #  Attribut (vairabel)
        self.value = value
    
    # Vanlig metod i en klass
    
    def show(self):                      
        return f"{self.suit} {self.value}"
    
    
    def __str__(self):                          # Dundermetod (double__underscore)
        return f"{self.suit} {self.value}"      # Attribut (variabel)
    
    
    def __repr__(self):                         # Dundermetod (represent(?))
        return f"{self.suit}{self.value}"


class Deck:
    def __init__(self, cards=None): 
        if cards is None:
            cards = []
        self.cards = cards
    

    @staticmethod
    def make_deck():
        cards = []
        suits = ["♠", "♥", "♣", "♦"]
        values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        
        
        for suit in suits:  # 4 suits  
            for value in values: # 13 values per suit
                cards.append(Card(suit, value))
        
        return cards

os.system("cls")
#def create_deck():
#    #cards = []
    
 #   suits = ["♠", "♥", "♣", "♦"]
 #   values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    
#    for suit in suits:
#        for value in values:
#            cards.append(Card(suit, value))
#    return cards

    
os.system("cls" if os.name=="nt" else "clear")


cards = Deck.make_deck()
deck = Deck(cards)
for cards in cards:
        print((cards))
        

