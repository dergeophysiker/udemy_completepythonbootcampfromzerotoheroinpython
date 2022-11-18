#CARD
# SUIT RANK VALUE

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit,rank):
        self.suit = suit
        self.rank = rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

######################################################

'''
twi_hearts=Card("Herts","Two")
three_of_clubs=Card("Clubs",'Three')

print(three_of_clubs)
print(three_of_clubs.value)
'''
######################################################

class Deck:
    def __init__(self):
        self.all_cards=[]

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
        #self.shuffle()

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
######################################################
'''
new_deck=Deck()
#print(new_deck.all_cards[0])
mycard=new_deck.deal_one()
print(mycard)
'''
######################################################

class Player:

    def __init__(self,name):
        self.name = name
        self.all_cards=[]

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'

'''
new_player=Player('Jose')
print(new_player)
new_player.add_cards(mycard)
new_player.add_cards(mycard)
new_player.add_cards(mycard)
new_player.add_cards(mycard)

print(new_player)
print(new_player.all_cards[0])
print(new_player.all_cards[1])
print(new_player.all_cards[2])
print(new_player.all_cards[3])

new_player.remove_one()
print(new_player)
'''
######################################################

new_deck=Deck()
new_deck.shuffle()

player_one=Player('player_one')
player_two=Player('player_two')
#print(new_deck.all_cards[0])

while len(new_deck.all_cards) != 0:
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(new_deck.all_cards)
print(len(player_one.all_cards))
print(len(player_two.all_cards))


round_num = 0
game_on = True

while game_on:
    round_num+=1

    print(f'Round {round_num}')

    if len(player_one.all_cards)==0:
        print('player one out of cards, so player two wins!')
        game_on = False
        break

    if len(player_two.all_cards)==0:
        print('player two out of cards, so player one wins!')
        game_on = False
        break

    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())

    print(player_one_cards[0])
    print(player_two_cards[0])
    
    name = input("Give me input")


    at_war = True
    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        
        else:
            print('WAR!')
            print(str(player_one_cards[-1].value) + " " + str(player_two_cards[-1].value))
            print(len(player_two.all_cards))
            print(len(player_one.all_cards))
            print(len(player_one_cards))
            print(len(player_two_cards))
            
            if len(player_one.all_cards) < 5:
                
                print('Player ONE unable to declare war so PLAYER TWO wins!')
                game_on=False
                break
            elif len(player_two.all_cards) < 5:
                
                print('Player TWO unable to declare war so PLAYER ONE wins!')
                game_on=False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
