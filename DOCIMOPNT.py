
import os
import time
import os


def clear():
    os.system('cls' if os.name =='nt' else 'clear')

clear()
class school:
    def __init__(self,name,clase,national,taime):
        self.name=name
        self.clase=clase
        self.national=national
        self.taime=taime

    def display_info(self):
        print(f'your nam is :{self.name}')
        print(f'your  is :{self.clase}')
        print(f'your  is :{self.national}')
        print(f'your  is :{self.taime}')
def mo3tiat():
    name=input(f"your name is :")
    calse=input(f"your clase is :")
    national=input(f"your national is :")
    taime=input(f"your taime is :")
    return school(name,calse,national,taime)
    
users=[]

while True:
    print("1. add new user\n2. display all\n3. exit")
    clek=input("enter your choice: ")
    if clek == '1':
        users.append(mo3tiat())
        print("User added successfully!\n")
        time.sleep(3)
        #fgjfjgj
    elif clek=='2':
        if users:
            print("Displaying all users:")
            for user in users:
                user.display_info()
        else:   
            print("No users available.\n")
            time.sleep(3)
        #fgjfjjj
    elif clek=='3':
        print("Exiting the program.")
        break  
    else :
        print("Invalid choice. Please try again.\n")
        time.sleep(3) 