
my_book=[]
lev_book=[]
#my book lest
start=input("are you hav a leve book 'yes'-'no'").lower()
while True :
    if start=='yes':   
        nam_book=input("enter nam of book your havet: ").lower()
        print("-"*22)

        if nam_book =='':
            break
        else:
            my_book.append(nam_book)
    else:
        print("Exiting as there are no books.")
        exit()            

print(f"your lest book havet is :{' + '.join(my_book)}")
print("-"*22)

#leve  book lest
while True :   
    live_book=input("enter lrive of book your lavet: ").lower()
    print("-"*22)

    if live_book =='':
        break
    else:
        lev_book.append(live_book)

print(f"your liev book havet is: {' + '.join(lev_book)}\n--------------------")
print("-"*22)

#book you bay it 
while True :   
    bay_book=input("enter name of book do you buy it :==\n*********").lower()
    if bay_book =='':
        break
    elif bay_book not in lev_book:
        my_book.append(bay_book)
    elif bay_book in lev_book:
        my_book.append(bay_book)
        lev_book.remove(bay_book)
    else:
        break

print (f"yor har a {len(my_book)} ,book \n and stel a {len(lev_book)},book")
print(f"your  book  is:: {' + '.join(my_book)}\nand you liv book is:{' + '.join(lev_book)}:")
