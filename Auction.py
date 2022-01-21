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
highest_bid=0  
for key in name_list:
    bid_amount=int(name_list[key] ) 
    if bid_amount>highest_bid:
        highest_bid=bid_amount
        winner_name=key  

 
print(f"{winner_name} is Winner with bid {highest_bid}/- ")

   
    
