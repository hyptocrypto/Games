'''Simple card game of war  '''

import random 

# Set up lists and Dictionaries from which you can create cards and a deck
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
             'Queen':12, 'King':13, 'Ace':14}

# Class to Create a single card 
class Card():
    
    def __init__(self,suit,rank):
       
        self.suit = suit 
        self.rank = rank 
        
        
    def __str__(self):
        return self.rank + ' Of ' + self.suit

# Class to make a full deck of cards using the Card class 
class Deck():
    
    def __init__(self):
        
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
                
    # Method to print the content of the deck 
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return deck_comp
    
    # Method to shuffle the sorted deck 
    def shuffle(self):
        random.shuffle(self.deck)

    # Method to deal a single card    
    def deal(self):
        single_card = self.deck.pop()
        return single_card

# Check to see what player wins the current hand
def who_wins():
    
  
    if Player.value > Dealer.value:
        Player.Points += 1
        print('\nPlayer wins!')
    elif Dealer.value > Player.value:
        print('\nDealer wins!')
        Dealer.Points += 1 
    elif Player.value == Dealer.value:
        war()
    
    
    print(f'\nDealer has {Dealer.Points} points.')
    print(f'Player has {Player.Points} points.')
    print('\n\n')



# Class that acts as the current hand(single card) the payers have
class Hand():

    def __init__(self):
        
        self.card = []
        self.value = 0
        self.Points = 0

    # Method to take a single card from the deal() method  
    def take_card(self,card):
        
        self.card.append(card)
        
        self.value = values[card.rank]

    # Method to print the contents of hand 
    def __str__(self):
        output = ''
        for single_card in self.card:
            output += str(f'  {single_card}') +'\n'
        return output




# If both players have a card of even vlaue then you go to war. In war you choose 3 cards and whoevers thrid card is of higher value wins 3 points
def war():
    print('--------------\n\
    WAR!!!\n-------------')
    player_war_hand = Hand()
    dealer_war_hand = Hand()
    
    pulled_card = game_deck.deal()
    player_war_hand.take_card(pulled_card)
    
    pulled_card = game_deck.deal()
    dealer_war_hand.take_card(pulled_card)
    
    pulled_card = game_deck.deal()
    player_war_hand.take_card(pulled_card)
    
    pulled_card = game_deck.deal()
    dealer_war_hand.take_card(pulled_card)
    
    pulled_card = game_deck.deal()
    player_war_hand.take_card(pulled_card)
    
    pulled_card = game_deck.deal()
    dealer_war_hand.take_card(pulled_card)
    

    print('Dealer has')
    print(dealer_war_hand)
    print('Player has')
    print(player_war_hand)
    
    if player_war_hand.value > dealer_war_hand.value:
        Player.Points += 3
        print('Player wins!')
    elif dealer_war_hand.value > player_war_hand.value:
        print('Dealer wins!')
        Dealer.Points += 3  
    elif Player.value == Dealer.value:
        war2()


# If on the first round of War the thrid cards drawn were of equal value then you play war again!
def war2():
    print('--------------\n\
    WAR!!!\n-------------')
    player_war_hand = Hand()
    dealer_war_hand = Hand()
    
    pulled_card = game_deck.deal()
    player_war_hand.take_card(pulled_card)
    
    pulled_card = game_deck.deal()
    dealer_war_hand.take_card(pulled_card)
    
    pulled_card = game_deck.deal()
    player_war_hand.take_card(pulled_card)
    
    pulled_card = game_deck.deal()
    dealer_war_hand.take_card(pulled_card)
    
    pulled_card = game_deck.deal()
    player_war_hand.take_card(pulled_card)
    
    pulled_card = game_deck.deal()
    dealer_war_hand.take_card(pulled_card)
    

    print('Dealer has')
    print(dealer_war_hand)
    print('Player has')
    print(player_war_hand)
    
    if player_war_hand.value > dealer_war_hand.value:
        Player.Points += 3
        print('Player wins!')
    elif dealer_war_hand.value > player_war_hand.value:
        print('Dealer wins!')
        Dealer.Points += 3






       ####### GAME LOGIC ########





print('\nWelcome to WAR!\nYou and the dealer draw a card and show them. High card wins.\n\
Winning is +1 Point.\nGood Luck!\n\n\n\n')

print('Ready to play??')
answer = input('')
print('\n\n')

#Create Deck using the Deck class and shuffle it using the shuffle method 
game_deck = Deck()
game_deck.shuffle()



# Set up the player and Dealer hands using the hand class 
Dealer = Hand()
Player = Hand()

Dealer.Points = 0
Player.Points = 0

# Use a try block to pull cards for the deck and play the game untill the deck is empty and pulling a card returns and IndexError
try:
    for x in range(30):   
        pulled_card = game_deck.deal()
        Dealer.take_card(pulled_card)
        print(f'Dealer has a {pulled_card}')

        print('\n           VS \n')

        pulled_card = game_deck.deal()
        Player.take_card(pulled_card)
        print(f'Player has a {pulled_card}')


        who_wins()
        

        again = input('Ready for another hand? \n ')
        print('-------------------------------- \n')        
        
except IndexError:
    print('The deck is empty!\nWhoever has the most points wins!!!')

    
finally:
    print('Thanks for playing\n\n')



