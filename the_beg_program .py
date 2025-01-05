import random
import os
def clear():
    os.system('cls' if os.name =='nt' else 'clear')
clear()
#creat the cracter
def cracter():
    super_hero = ["Superman","Batman","Spider-Man","Wonder Woman","Iron Man","Hulk","Thor","Black Panther","Captain America","Flash"]
    games = ["Call of Duty", "Minecraft", "Fortnite", "GTA V", "League of Legends"]
    basket = ["Michael Jordan", "LeBron James", "Kobe Bryant", "Stephen Curry", "Shaquille O'Neal"]
    anime = ["Naruto", "Dragon Ball", "Attack on Titan", "One Piece", "Demon Slayer"]
    football = ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr", "Kylian Mbappe", "Pele"]
    return super_hero,games,basket,anime,football
   #chosing a talmi7:

def talmi7(ia_chooes,leter,namber):
    
    talmih=input("Do you want  talmi7 Enter 1:").lower()
    print("*"*33)
    
    if talmih=='1' and namber>0:
        cor=[]
        
        for x in ia_chooes:
            if x not in leter not in cor:
                namber-=1
                print(f'The leter is ("{x}") \n You have a "{namber}" Talmi7 "') 
                print("*"*33)  
                cor.append(x)
                break 

    return namber,talmih ,cor



#sponer
exit=True
while exit:
    
    print("What is your favorite category?")
    print("1. Superhero")
    print("2. Games")
    print("3. Basketball Players")
    print("4. Anime")
    print("5. Football Players")
 
    

    user=input("Enter the number of your favorite category: ")
    clear()
    #fanct
    super_hero, games, basket, anime, football = cracter()
    if user == "1":
        ia_chooes = random.choice(super_hero).lower()
        print(f'You choese Super_hero')
    elif user == "2":
        ia_chooes = random.choice(games).lower()
        print(f'You choese Games')
    elif user == "3":
        ia_chooes = random.choice(basket).lower()
        print(f'You choese Basket')
    elif user == "4":
        ia_chooes = random.choice(anime).lower()
        print(f'You choese Anime')
    elif user == "5":
        ia_chooes = random.choice(football).lower()
        print(f'You choese Football')
    else:
        print("Invalid choice 1 to 5 !")
        continue
    #chooes ia random
    namber=3
    clear()
    chooes ='-'*len(ia_chooes)
    #appeand the chosse 
    leter=[]
    for let in ia_chooes:
        if let.isalpha():
            leter.append('-')
        else:
            leter.append(let)
    # play 
    attempts = len(ia_chooes) - 2 
    print(f"Welcome to the game! You have {attempts} attempts to guess your chooes.")
    print("Enter one letter at a time.")
    print(f"Guess that : {' '.join(leter)}")
    print(ia_chooes)

    #my leter chooes

    while ('-') in (leter) and (attempts>0):
        my_chooes=input('Enter a single letter:').lower()
        clear()
        if len(my_chooes)>1 or not my_chooes.isalpha():
            print("Invalid input! Please enter a single letter.")
            
            continue

        if my_chooes in ia_chooes:
            
            print(f"Good job! The letter '{my_chooes}' is in the word.")    
            for posichen in range(len(chooes)):
                if my_chooes == ia_chooes[posichen]:
                    leter[posichen]=my_chooes
                    print("*"*33)
        else:
            print("*"*33)
            print(f"Oops! The letter '{my_chooes}' is not in the word.")
            attempts -= 1
            talmi7(ia_chooes,leter,namber)
            print("*"*33)
            

        # the loser
        print(f"Current word: {' '.join(leter)}")
        print(f"Remaining attempts: {attempts}")
        print("-" * 20)


    # finale chense
    if "-" not in leter:
        print(f"Congratulations! You guessed the word: {ia_chooes.capitalize()}")
    else:
        print(f"Game Over! The word was: {ia_chooes.capitalize()}")
    
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thank you for playing!")
        break