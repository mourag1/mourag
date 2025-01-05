#IA seystem
import random
ia=random.random()*2
while True:
  #presantacio to chachter
  print ("hello in that page\n ")
  nam=(input('hi wat is you nam:\n'))
  print(f'hi Ms.{nam}\n')
  reade=input(f'ms.{nam} my and you play in game are you readn  (yes)or(no)\n').lower()

  #read to play (yes) ou (no)
  if reade=='yes':
    print('Great! Let\'s start!')
    door=input('yor are in a room and you have 3 doors to ran in taht rom cous in thet doors (red),(blc),(blan)\n').lower()#level in 
    if door=='red':
      print('your faond a dragon your dead\n')
      
    elif door=='blc':
      print('you fall from a great height you are dead\n')
      
    elif door=='blan':    #level door1
      sword=input('I came out of the room and found three weapons (pistol), (sword) and (saw). How do you open the gate?\n').lower()
    else:
      print('soory your choice is not in the list you are dead\n')
      
  elif reade=='no':
    print("Ok come back when you're ready\n")
    
  else:
    print('soory your choics is not in the list\n ooo!, thinking outside the box is good, but unfortunately you died. Follow the instructions.\n')


  #reade to game level 2

  if sword==('saw'):
    print('Used the (saw) but it didn\'t work and activated one of the hidden')
  elif sword==('sword'):
    play=input("you fauund a man ask you to play a game with him (yes) or (no)\n").lower()
    if play==('no'):
      print('The unknown person turns into a ghoul and eats you\n')
    elif play==('yes'):
      mi=input('We will play the coin game choose (heads) or (tails)\n').lower()
      if ia<0.5 and mi==('heads'):
        print('your win')
      elif ia>0.5 and mi==('tails'):
        print('you win')
      else:
        print ('youu lose I\'m hongry')

  print ('tanke you for playing with me and good bye')
  exit()
