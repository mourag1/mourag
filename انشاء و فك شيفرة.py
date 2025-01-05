import string
chosse=input("Please enter '1' for encryption or '2' for decryption: ")
key=int(input("enter key:"))
texter=input("enter to:")
alhabe=string.ascii_lowercase
texte=""
if chosse == '2':
    key = -key
#
while True:
    for box in texter:
        if box.lower() in alhabe:
            makan=(alhabe.index(box.lower())+key)%26
            newtexte=alhabe[makan]
            if box.isupper():
                newtexte=newtexte.upper()
            texte+=newtexte
        else:
            texte+=box
        
    print(f"you new texter is :={texte}")
    stop=input("enter ok to stop")
    if stop =="":
        break
    print("You entered:", stop)

