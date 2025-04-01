#Rock Paper Sijer
print("Let's start the game!!!!")
import random
computer=random.choice([1,2,3])
'''
rock=1
paper=2
sijer=3
'''
name=input("Enter your name:")
print("Rock for r\nPaper for p\nSijer for s")
print("Enter your choice")
you1=input()

dict1={"r":1,"p":2,"s":3}
you=dict1[you1]
dic1={1:"Rock",2:"Paper",3:"Sijer"}
print(f"Your choice is {dic1[you]}\nComputer choice is {dic1[computer]}")
#print(f"Your choice is {dic1[you]} and computer choice is {dic1.get(computer)}")
if(computer==you):
      print("Both you and the computer had the same choice")
else:
      if(computer==1 and you==2):
          print(f"You win, {name}!!")
      elif(computer==1 and you==3):
          print(f"You lose, {name}!!")
      elif(computer==2 and you==1):
          print(f"You loose, {name}!!")
      elif(computer==2 and you==3):
          print(f"You win, {name}!!")
      elif(computer==3 and you==1):
          print(f"You win, {name}!!")
      elif(computer==3 and you==2):
          print(f"You loose {name}!!")
      else:
          print("You enter something wrong")
          
