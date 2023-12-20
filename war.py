import random

# Global Variables
# Card suites,rank and value
suites=("Clubs","Diamonds","Hearts","Spades")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

# Creating a class to add rank, suite and value as instances
class Card:
    k=[]
    # method to create attributes
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        Card.k.append(self)
    # method to print attributes
    def __repr__(self):
        return f"Card({self.suit},{self.rank},{self.value})"
    
# creating a class Deck to add objects of all cards
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suite in suites:
            for rank in ranks:
                self.all_cards.append(Card(suite,rank))
    def shuffle(self):
        '''To shuffle the deck.'''
        random.shuffle(self.all_cards)
    def deal(self):
        return self.all_cards.pop()

#Creaing a player class
class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove(self):
        return self.all_cards.pop(0)
    def add(self,removed_card):
        if type(removed_card)==type([]):
            self.all_cards.extend(removed_card)
        else:
            self.all_cards.append(removed_card)
    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} which are {self.all_cards}"

#Creating new deck
game_on=True
new_deck=Deck()
new_deck.shuffle()

#players
Player_1=Player("One")
Player_2=Player("Two")

#diving the cards
for i in range(26):
    Player_1.add(new_deck.deal())
    Player_2.add(new_deck.deal())

round=0

#Game logic
while game_on:
    round=round+1
    print(f"round {round}")
    
    #win-loose
    if len(Player_1.all_cards)==0:
        print("Player 1 out of cards! Player 2 wins!")
        game_on=False
        break
    elif len(Player_2.all_cards)==0:
        print("Player 2 out of cards! Player 1 wins!")
        game_on=False
        break

    #creating cards put on table:
    Player1_cards=[]
    Player1_cards.append(Player_1.remove())
    Player2_cards=[]
    Player2_cards.append(Player_2.remove())

    #war logic
    war=True
    while war:
        if Player1_cards[-1].value > Player2_cards[-1].value:
            Player_1.add(Player1_cards)
            Player_1.add(Player2_cards)
            war=False
        elif Player1_cards[-1].value < Player2_cards[-1].value:
            Player_2.add(Player1_cards)
            Player_2.add(Player2_cards)
            war=False
        else:
            print('WAR!')
        
            if len(Player_1.all_cards) < 5:
                game_on = False
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                break

            elif len(Player_2.all_cards) < 5:
                game_on = False
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    Player1_cards.append(Player_1.remove())
    
                    Player2_cards.append(Player_2.remove())  