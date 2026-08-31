import random,time,winsound
class Items:
  def __init__ (self,price,amount,name):
    self.price = price
    self.amount = amount
    self.name = name
Exit_Condition = False
Buying_Input =""
User_Input_Starting_Game =""
BreakTime = 15
Stated_Games = 0
i = 0
Food_List = ["Salad","Lemon","Banana","Strawberry","Apple","Ice","Vanilla Cream","Cheese","Rice","Soup","Potato","Fried egg","Orange","Cream"]
Money = 0
anger = 0
Scissors = Items(300,0,"scissors")
Candy = Items(800,0,"candy")
Knife = Items(2000,0,"knife")
Want_To_Eat = Food_List[random.randint(0,13)]
Showing = {Food_List[random.randint(0,13)],Food_List[random.randint(0,13)],Want_To_Eat}
Angry_Food_List = ["BRAIN","EYE","HAND"]
Int_Input = 0
Event_Sack = 0
Event_Starting_Rate = 0
Hiding1 = 0 #is used to print "(???)"
Hiding2 = 0
Used_Scissors = 0
Used_knife = 0
True_Ending = 0
#start
print("Welcome to the Kitchen")
while Used_knife != 1:
  time.sleep(0.5)
  print("1.Shop")
  print("2.Game")
  print("3.Credit")
  print("4.How to play")
  print(f"Money: {Money}")
  time.sleep(0.5)
  while True:
#User Menu input
    User_Input_Starting_Game = input("Where would you go? ").strip().lower()
    if User_Input_Starting_Game != "1" and User_Input_Starting_Game != "2" and User_Input_Starting_Game != "game" and User_Input_Starting_Game != "shop" and User_Input_Starting_Game == "3" and User_Input_Starting_Game == "credit":
      print(User_Input_Starting_Game)
      print("ENTER CORRECT NUMBER OF PLACE NAME")
      continue
    else:
      break    
#Credit
  if User_Input_Starting_Game == "3" or User_Input_Starting_Game == "credit":
      time.sleep(1)
      print("MADE BY NAZON")
      print("(ft.mimo)")
      print("")
#How to play
  if User_Input_Starting_Game == "4" or User_Input_Starting_Game == "how to play":
      time.sleep(1)
      print("Enter food number to feed Mr.tomato")
      time.sleep(0.5)
      print("You can earn money when you fed correct food")
      time.sleep(0.5)
      print("With money, you can buy items,which can ease Game Play")   
      time.sleep(0.5)
      print("Enter 'item' to use items in game") 
#Game
  if (User_Input_Starting_Game == "2" or User_Input_Starting_Game == "game") and Stated_Games == 0:
    #Death after true ending
    if True_Ending == 1:
      time.sleep(10)
      print("Mr.tomato: I Said You Never Come Back,FOREVER")
      time.sleep(1)
      print("Mr.tomato: Why Did You Ignore Me?")
      time.sleep(1)
      print("Mr.tomato: I will make you pay for this")
      time.sleep(1)
      print(winsound.Beep(2000,3500))
      break
    print("--------In Game--------")
    time.sleep(0.8)
    print("Mr.tomato: Hi")
    time.sleep(0.9)
    print("Mr.tomato: I'm MR.tomato")
    time.sleep(1)
    print("Mr.tomato: Having no hands,I hired you to feed me")
    time.sleep(2)
    print("Mr.tomato: Be ready")
    time.sleep(0.5)
    Stated_Games += 1
  elif User_Input_Starting_Game == "2" and Stated_Games != 0:
    print("Mr.tomato: Welcome Back.")
    print("")
    time.sleep(0.5)
    Stated_Games += 1
#Playing Process  
  while User_Input_Starting_Game == "2":
    while True:
      if len(Showing) < 3:
        Showing = {Food_List[random.randint(0,13)],Food_List[random.randint(0,13)]}
        Showing.add(Want_To_Eat)
      else:
       break
    Showing_List = list(Showing)
    Real_Having = Showing_List.copy()
    time.sleep(0.5)
    print(f"I'd like to eat {Want_To_Eat}")
    print(f"ANGER: {anger}")
    print(f"Left Food: {BreakTime}")
    if Stated_Games > 1 and Event_Sack == 1:#Event sack
      Hiding1 = random.randint(0,2)
      Hiding2 = random.randint(0,2)
      while Hiding1 == Hiding2:
        Hiding2 = random.randint(0,2)
      Showing_List[Hiding1] = "(???)"
      Showing_List[Hiding2] = "(???)"
    if Used_Scissors == 1:
      for i in range(1,4):
        print(f"{i}.{Real_Having[i-1]}")
        Used_Scissors = 0
    else:
      for i in range(1,4):
        print(f"{i}.{Showing_List[i-1]}")
        Used_Scissors = 0
    try:
      Giving = input("Enter Number or 'item'(To use items): ").strip().lower()
      if Giving == "item":
        print(f"Scissors: {Scissors.amount}")
        print(f"Candy: {Candy.amount}")
        if Knife.amount == 1:
          print(f"Knife: {Knife.amount}")
        elif Knife.amount == 0:
          print(f"???: {Knife.amount}")
        Item_Using_Input = input("Which item would you use?").strip().lower()
        if Item_Using_Input != "scissors" and Item_Using_Input != "candy" and Item_Using_Input != "knife":
          print("No Item Used")
          time.sleep(0.5)
          continue
        #scissors event
        if Item_Using_Input == "scissors" and Scissors.amount > 0 and Stated_Games > 0 and Event_Sack == 1:
          print("Used 'scissors'")
          Scissors.amount -= 1
          Used_Scissors = 1
          continue
        if Item_Using_Input == "scissors" and Scissors.amount == 0:
          print("You dont have scissors")
          continue
        #candy event
        if Item_Using_Input == "candy" and Candy.amount > 0:
          time.sleep(1)
          print("Mr.tomato: Umm...delicious")
          Candy.amount -= 1
          anger -= 3
          if anger < 0:
            anger = 0
          continue
        if Item_Using_Input == "candy" and Candy.amount == 0:
          print("You dont have candy")
          continue
        #knife event  
        if Item_Using_Input == "knife" and Knife.amount == 1:
          time.sleep(1)
          print("Mr.tomato: Oh")
          time.sleep(1)
          print("Mr.tomato: I didn't think that you would kill me")
          time.sleep(2)
          print("Mr.tomato: You won,for now")
          Used_knife = 1
          break
      else:  
        Int_Input = int(Giving)
      if Int_Input > 3:
        print("Select numbers between 1~3")
        print("")
        continue
    except ValueError:
      print("Please enter 'Number'")
      continue  
    if Real_Having[Int_Input-1] == Want_To_Eat:
      time.sleep(1)
      Money += 75
      BreakTime -= 1
      Event_Sack = 0
      if Stated_Games > 1:
        Event_Starting_Rate = random.randint(0,100)
        if Event_Starting_Rate > 65:
          Event_Sack = 1
    else:
      time.sleep(1)
      print("Mr.tomato: I'd not asked This")
      Event_Sack = 0
      anger += 1
      BreakTime -= 1
      Money -= 75
#GAME OVER
    if anger >= 10:
      print("Mr.tomato: YOU ARE THE WORST PERSON I HAVE EVER SEEN")
      time.sleep(1)
      print("Mr.tomato: DOING THIS SIMPLE WORK IS TOO HARD FOR YOU?")
      time.sleep(1)

      break
#BREAK TIME
    if BreakTime == 0 or BreakTime < 0:
      time.sleep(0.5)
      print("Mr.tomato: Ok,I'm full for now")
      time.sleep(1)
      print("Mr.tomato: Come back later if I become hungry")
      time.sleep(2)
      print("Mr.tomato: See you later")
      BreakTime = 15 + Stated_Games * 5
      if BreakTime > 40:
        BreakTime = 40
      break
    Want_To_Eat = Food_List[random.randint(0,13)]
    Showing = {Food_List[random.randint(0,13)],Food_List[random.randint(0,13)],Want_To_Eat}
    print("")
    if Stated_Games == 7 and anger == 0:
      print("Mr.tomato: Wow,you were greater than I thought")
      time.sleep(1)
      print("Mr.tomato: I was surprised")
      time.sleep(1)
      print("Mr.tomato: I will give you a gift,a note that I couldn't understand")
      time.sleep(1) 
      print("Mr.tomato: I think that you will understand it")
      time.sleep(1)
      print("Mr.tomato: Goodbye and never come back")
      #SHOPPING
  while User_Input_Starting_Game == "1" or User_Input_Starting_Game == "shop":
    if Exit_Condition == False:
      print("--------SHOP--------")
      print(f"Scissors: {Scissors.price}, you have {Scissors.amount} scissor(s)")
      print(f"Candy: {Candy.price}, you have {Candy.amount} candy(s)")
      print(f"???: {Knife.price}, you have {Knife.amount} amount of something")
      print("1.Scissors")
      print("2.Candy")
      print("3.???")
      print("4.exit")
      print(f"Money: {Money}")
      time.sleep(0.7)
      Buying_Input =input("what would you buy? ")
      if Buying_Input == "1":
        if Money >= Scissors.price:
          Money -= Scissors.price
          Scissors.amount += 1
          print("Purchased Scissors!")
          print("")
        else:
          print("You don't have enough money")
          print("")
      elif Buying_Input == "2":
        if Money >= Candy.price:
          Money -= Candy.price
          Candy.amount += 1
          print("Purchased Candy!")
          print("")
        else:
          print("You don't have enough money")
          print("")
      elif Buying_Input == "3":
        if Money >= Knife.price:
          if Knife.amount == 1:
            print("You already have knife")
            break
          Money -= Knife.price
          Knife.amount += 1
          print("Purchased 'Knife'!")
          print("")
        else:
          print("You don't have enough money")
          print("")
      if Buying_Input == "4":
          Exit_Condition = True
    elif Exit_Condition == True:
      Exit_Condition == False
      break
