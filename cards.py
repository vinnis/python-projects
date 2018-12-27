import random
print ("there are 4 types of deck available to play namely diamond, hearts, club, spades")
nod=input("number of decks you want? ")
naofd=[]
if int(nod)>1:
    for i in range(1,int(nod)+1):
        naofd.append(input("name of the {} deck you want ".format(i)))
else:
        naofd.append(input("name of the {} deck you want ".format(i)))

nop=input("enter number of players who will play ")
player=[]
if int(nop)>1:
    for i in range(0,int(nop)):
        player.append(input("enter name of the player here "))
        
else:
        print("we cannot play game with 1 player")
print ("name of the {0} players are: {1}".format(len(player),player))

diamond=[]
hearts=[]
club=[]
spades=[]
print ("number of decks inputted are{}".format(nod))
for i in naofd:        
    print("names are {}".format(i))
    #if 'diamond' in naofd:
    if i == 'diamond':
        word='d'
        for i in range(1,14):
            word='d'+str(i)
            diamond.append(word)
    #elif 'club' in naofd:
    elif i == 'club':   
        word='c'
        for i in range(1,14):
            word='c'+str(i)
            club.append(word)
    #elif 'spades' in naofd:
    elif i == 'spades':
        word='s'
        for i in range(1,14):
            word='s'+str(i)
            spades.append(word)
    #elif 'hearts' in naofd:
    elif i == 'hearts':
        word='h'
        for i in range(1,14):
            word='h'+str(i)
            hearts.append(word)
    else:
        print ('not a valid deck name')
#print ('decks as follows \n',diamond,spades,club,hearts)
total_cards=[]
for i in diamond:
    total_cards.append(i)

for i in club:
    total_cards.append(i)

for i in spades:
    total_cards.append(i)

for i in hearts:
    total_cards.append(i)

print ("total cards are {}".format(total_cards))
distribution=len(total_cards)//len(player)
for i in range(0,len(player)):
    print ("{} got following cards".format(player[i]))
    player[i]=[]
    for j in range(0,distribution):
        x=random.choice(total_cards)
        player[i].append(x)
        total_cards.remove(x)
        print(player[i][j])
        

        
