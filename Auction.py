from art import logo
import os
def clear():
  
    # for windows
    
     _ = os.system('cls')
  
print(logo)
print('WELCOME FOR THE AUCTION')
name=input("ENTER YOUR NAME: \n")
bid=input("ENTER YOUR BID :  \n")
name_list={name:bid}
clear()
#ASK ANY OTHER PEOPLE FOR BIDING

others=input("if there are more people to bid enter  'YES'or 'NO' : \n").lower()
while others=="yes":
    if others=="yes":
        name=input("ENTER YOUR NAME: \n")
        bid=input("ENTER YOUR BID :  \n")
        name_list[name]=bid
        clear()
    others=input("if there are more people to bid enter  'YES'or 'NO' : \n").lower()    
if others=="no":
    for key in name_list:
     var=max(key)
     winner_amount=name_list[key]
     winner_name=key
    
print(f"Winner of Auction is {winner_name} with bid:{winner_amount}/-")