import random
class NumError(Exception):
  pass
print("Welcome to the Lottery!Guess the number and collect money")
print("matched 1 number:5$")
print("matched 2 numbers:30$")
print("matched 3 numbers:500$")
print("matched 4 numbers:1,000$!")
print("matched 5 numbers:7,000$!!")
print("matched all numbers:1,000,000$!!!")
moneyDic={0:0,1:5,2:30,3:100,4:500,5:1000,6:10000}
totalMoney=0
CollectedMoney=0
while True:
  UCNList=[]
  while len(UCNList)<6:
    try:
      UserChosenNumber=input("Choose your lottery number!: ")
      UserChosenNumber=int(UserChosenNumber)
      if UserChosenNumber>45 or UserChosenNumber<1:
        raise NumError
      if UserChosenNumber in UCNList:
        print("you already have chosen that number!")
        continue
      UCNList.append(UserChosenNumber)
    except ValueError:
      print("Please enter number")
      continue
    except NumError:
      print("You have chosen wrong number!Please try again(1~45)")
      continue

  print(f"You chose {sorted(UCNList)}")
  numList=set()
  while len(numList)<6:
    Numbers=random.randint(1,45)
    numList.add(Numbers)
  print(f"Today's Lottery Number is {list(numList)}!")
  Common=list(set(UCNList)&set(numList))
  print(f"Matched {len(Common)} number(s)!")
  CollectedMoney=moneyDic.get(len(Common))
  print(f"Collected {CollectedMoney}$!")
  if len(Common)==6:
    print("HOW??")
  elif len(Common)==5:
    print("You are Very Lucky!")
  elif len(Common)==4:
    print("That was Nice!")
  elif len(Common)==0:
    print("That's so Bad!")
  totalMoney=totalMoney+CollectedMoney
  play_again = input("\nDo you want to play again for 3$? (yes/no): ").lower()
  if play_again != 'yes' and play_again!='y' and play_again!='ye':
    break
  else:
    totalMoney-=3
print(f"You have totally collected {totalMoney}$!")
