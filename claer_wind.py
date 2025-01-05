import os
import random
import time

def cl():
    os.system("cls")
 
book={}

def add_book():
    while True:
        book_id=input ("enter book Id : ").lower()
        if book_id in book:
            print("the id in lest chenget ")
            add_book()

        book_nam=input ("enter name of book: ").lower()
        book_date=input ("enter date of book: ").lower()

        while not  book_date.isdigit(): book_date = input ("enter a date: ")

        book[book_id]={"nam":book_nam,'date':book_date,'active':True} 

        print(f'the book "{book[book_id]['nam']}" is sacfoct.\n the id is: {book_id} memeber it\n')

        nader=input("do you add a nader book enter 'y': ").lower()
        if nader != 'y':
            break

def tik_book():
    while True:
        book_id=input("enter book id to tik it ")
        if book_id in book and book[book_id]['active']==True:
            print(f"the book is '{book[book_id]['nam']}' \n are you oantid ")
            choer=input("are you choer tikrt the book 'y'").lower()
            if choer =='y':
                book[book_id]['active']=False
                print("the book tik ")
        elif book_id not in book:
            print('the book not faond ples cheak your id')
            
        elif not  book[book_id]['active']==True:
            print("the book is tik kit pleas tray nader time!!")
            
        nader=input("Do you Tik a Nader book enter 'y': ").lower()
        if nader != 'y':
            break
    
def edit_book():
    while True:
        book_id=input("enter id book to edit ")
        if book_id in book and book[book_id]['active']==True:
            new_nam=input('enter a new nam af book : ')
            new_date=input('enter a new date af book : ')
            while not  new_date.isdigit(): new_date = input ("enter a date pleas: ")
            book[book_id]={"nam":new_nam,'date':new_date,'active':True} 
        elif book_id not in book:
            print('the book not faond ples cheak your id')
            continue
        elif not  book[book_id]['active']==True:
            print("the book is tik kit pleas tray nader time!!")
            continue

        nader=input("Do you Tik a Nader book enter 'y': ").lower()
        if nader != 'y':
            break        

def list_book():
    print(f"the laberi have a : {len(book)} book")
    
    print ("\n"*2)
    
    for list in book:
        i=book[list]
        print (f"the nam of book {list} is :{i['nam']}") 
        print (f"the date of  book {list} is :{i['date']}") 
        print (f"the active of book {list} is :{i['active']}") 
        print ("-"*22) 
        time.sleep(0.5)
    time.sleep(2)
    choe=input("do you go to mun: ")
        
while True:
    cl()
    print("Menu.............")
    print("1.Add book")
    print("2.Check out book")
    print("3.edit a book")
    print("4.List book")
    print("5.Exit")
    x=input("enter your choice 1 to 5: ")
    if x== "1" :
        add_book()
    elif x== "2" :
        tik_book()
    elif x== "3" :
        edit_book()
    elif x== "4" :
       list_book()
    elif x=='5':
        print("bye ...... ")
        break
    else:
        print('enter 1 to 5')
        continue
    
