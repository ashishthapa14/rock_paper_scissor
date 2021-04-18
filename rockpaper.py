import random,sys

print('ROCK','PAPER','SCISSOR')
print('Plzz open Your caps lock!')
#these things keep track of winning,losses and tie:
wins = 0
ties = 0
loss = 0

while True:   #Main loop
    print('%s Wins , %sLoss , %sTies' %(wins,loss,ties))
    while True:  #Player input loop
        print('Enter your move: '+ '(R)ock '+ '(P)aper '+ '(S)cissor '+ 'or '+'(Q)uit')
        player = input()
        if player == 'Q':
            sys.exit() #exit from the game:
        elif player == 'R' or player == 'S' or player == 'P':
            break
        print("Enter one of these: 'R' or 'P' or 'S' or 'Q' ")
    #Display playermove 
    if player == 'R':
        print('Rock versues ....')
    elif player == 'P':
        print('Paper versues....')
    elif player == 'S':
        print('Scicssor versues...')
    
    #Display Computermove:
    computer = random.randint(1,3)
    if computer == 1:
        computermove = 'R'
        print("Rock")
    elif computer  == 2:
        computermove = 'P'
        print("Paper")
    elif computer == 3:
        computermove = 'S'
        print("Scissor")
    
    #Display of win,loss,tie;
    if player == computermove:
        print("It's a Tie")
        ties = ties + 1
    elif player == 'R' and computermove == 'S':
        print('You win')
        wins = wins + 1
    elif player == 'P' and computermove == 'R':
        print("You win")
        wins = wins + 1
    elif player == 'S' and computermove == 'P':
        wins =wins + 1
        print("You win")
    elif player == 'R' and computermove == 'P':
        print('You loss')
        loss = loss+1
    elif player == 'S' and computermove == 'R':
        loss = loss+1
        print('You loss')
    elif player == 'P' and computermove == 'S':
        print('You loss')
        loss = loss + 1
