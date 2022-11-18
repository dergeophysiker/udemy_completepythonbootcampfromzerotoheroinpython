#CARD
# SUIT RANK VALUE

## Game Play
'''
To play a hand of Blackjack the following steps must be followed:
1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the Player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
11. Determine the winner and adjust the Player's chips accordingly
12. Ask the Player if they'd like to play again
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

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

    def __init__(self,name,cash):
        self.name = name
        self.cash=cash

    def __str__(self):
        return f'player {self.name} has {self.cash} dollars.'

######################################################
class Dealer(Player):
    def __init__(self,name,cash):
        Player.__init__(self,name,cash)
    

#######################################################
class Hand:

    def __init__(self):
        self.value = 0
        self.aces = 0
        self.cards=[]


    def add_card(self,new_card):
            self.cards.append(new_card)
            self.value=new_card.value + self.value
            if new_card.rank=="Ace":
                self.aces=self.aces+1
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value-=10
            self.aces-=1

#######################################################

def hit(somehand):
    somehand.add_card(new_deck.deal_one())
    somehand.adjust_for_ace()
    
#######################################################
def showplayercards():
    player_values=[(x.value) for x in playerhand.cards]
    player_cards = [str(x) for x in playerhand.cards]
    print(f'Player has {playerhand.value} from {player_values} => {player_cards}')


#######################################################
def showdealercards(partial=False):
    dealer_values=[(x.value) for x in dealerhand.cards]
    dealer_cards = [str(x) for x in dealerhand.cards]
    if not(partial):
        print(f'Dealer has {dealerhand.value} from {dealer_values} => {dealer_cards}')
    elif partial:
        print(f'Dealer has {dealer_values[0]} => {dealer_cards[0]}')
#######################################################
def losebet(bet,person):
    '''
    if isinstance(dealer, Dealer):
        pass
    else:
    '''       
    person.cash = person.cash - bet
#######################################################
def winbet(bet,person):
    person.cash = person.cash + bet
#######################################################


player=Player('Player',100)
dealer=Dealer('Dealer',0)


game_on = True

while game_on:
    new_deck=Deck()
    new_deck.shuffle()
    print(new_deck.all_cards[0])


    dealerhand=Hand()
    playerhand=Hand()

    print(player)
    print(dealer)



    bet = int(input("How much do you want to bet? "))

    if (100) <= 0:  #cash - bet
        print('You are out of money!')
        break
    else:
        print("Bet accepted!")
        pass

 
    playerhand.add_card(new_deck.deal_one())
    playerhand.add_card(new_deck.deal_one())
    
    dealerhand.add_card(new_deck.deal_one())
    dealerhand.add_card(new_deck.deal_one())
    
    print(len(new_deck.all_cards))
    
    showplayercards()
    showdealercards(True)
    print(isinstance(dealer, Dealer))
    print(isinstance(player, Dealer))
    print(isinstance(dealer, Player))
    print(isinstance(player, Player))

    #print(*playerhand.cards)   
    #playerhand.value=21
    #dealer_values=[11,10]


    stand=False
    bust=False
    blackjack=False
    initialdeal=True


    
    while not(stand) and not(bust):
        if playerhand.value == 21 and initialdeal==True:
            stand= True
            blackjack=True
            print("Player => BLACKJACK!")       
            break
        decision=str(input(("do you wish to hit (Y/N): ")))
        if decision == "Y":
            initialdeal=False
            hit(playerhand)
            showplayercards()
            if playerhand.value > 21:
                bust = True
                winbet(bet, dealer)
                losebet(bet, player)
                print("Player BUSTS!")
        elif decision == "N":
            stand=True
            break

    while stand and not(bust):
        if blackjack:
            stand=False
            showdealercards()
            if playerhand.value > dealerhand.value:
                winbet(bet, player)
                losebet(bet,dealer)
                print("Player Wins with BlackJack!")
            else:
                print("Push")
        elif dealerhand.value < 17:
            hit(dealerhand)
            showdealercards()
        elif dealerhand.value <= 21 and dealerhand.value >= 17:
            stand =False
            showdealercards()
            print("Dealer Stands")
            if playerhand.value > dealerhand.value:
                winbet(bet, player)
                losebet(bet,dealer)
                print("Player Wins")
            elif dealerhand.value > playerhand.value:
                winbet(bet,dealer)
                losebet(bet,player)
                print("Dealer Wins")
            else:
                print("Push")
        elif dealerhand.value > 21:
            bust=True
            showdealercards()
            winbet(bet, player)
            losebet(bet,dealer)
            print("Dealer BUSTS")

showplayercards()
showdealercards()
print(player.cash)
print(dealer.cash)
##################################

##################################
