import random,time
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
Int_Input = 0
Event_Sack = 0
Event_Starting_Rate = 0
Hiding1 = 0 #is used to print "(???)"
Hiding2 = 0
#start
print("Welcome to the Kitchen")
while True:
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
    print("--------In Game--------")
    time.sleep(0.8)
    print("Hi")
    time.sleep(0.9)
    print("I'm MR.tomato")
    time.sleep(1)
    print("Having no hands,I hired you to feed me")
    time.sleep(2)
    print("Be ready")
    time.sleep(0.5)
    Stated_Games += 1
  elif User_Input_Starting_Game == "2" and Stated_Games != 0:
    print("Welcome Back.")
    print("")
    time.sleep(0.5)
    Stated_Games += 1
#Playing Process  
  while User_Input_Starting_Game == "2":
    while True:
      if len(Showing) < 3:
        Showing = {Food_List[random.randint(0,13)],Food_List[random.randint(0,13)],Want_To_Eat}
      else:
       break
    Showing_List = list(Showing)
    Real_Having = Showing_List.copy()
    time.sleep(0.5)
    print(f"I'd like to eat {Want_To_Eat}")
    print(f"ANGER: {anger}")
    print(f"Left Food: {BreakTime}")
    if Stated_Games > 1 and Event_Sack == 1:#here i fixing
      Hiding1 = random.randint(0,2)
      Hiding2 = random.randint(0,2)
      while Hiding1 == Hiding2:
        Hiding2 = random.randint(0,2)
      Showing_List[Hiding1] = "(???)"
      Showing_List[Hiding2] = "(???)"
    for i in range(1,4):
      print(f"{i}.{Showing_List[i-1]}")
    try:
      Giving = input("Enter Number or 'item'(To use items): ").strip().lower()
      if Giving == "item":
        print(f"Scissors: {Scissors.amount}")
        print(f"Candy: {Candy.amount}")
        print(f"???: {Knife.amount}")#####HERE!!!!!!#####
        Item_Using_Input = input("Which item would you use?").strip().lower()
        if Item_Using_Input != "scissors" and Item_Using_Input != "candy" and Item_Using_Input != "???":
          print("No Item Used")
          time.sleep(0.5)
          continue
        if Item_Using_Input == "scissors" and Scissors.amount > 0 and Stated_Games > 0 and Event_Sack == 1:
          print("Used 'scissors'")
          Scissors.amount -= 1
          continue
#FROM HERE START FIXING:scissor event and rest of items event
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
        if Event_Starting_Rate > 75:
          Event_Sack = 1
    else:
      time.sleep(1)
      print("I'd not asked This")
      Event_Sack = 0
      anger += 1
      BreakTime -= 1
      Money -= 75
#GAME OVER
    if anger >= 10:
      print("YOU ARE THE WORST PERSON I HAVE EVER SEEN")
      time.sleep(1)
      print("GET OUT OF MY SIGHT,RIGHT NOW")
      time.sleep(1)
      break
#BREAK TIME
    if BreakTime == 0 or BreakTime < 0:
      time.sleep(0.5)
      print("Ok,I'm full for now")
      time.sleep(1)
      print("Come back later if I become hungry")
      time.sleep(2)
      print("See you later")
      BreakTime = 15 + Stated_Games * 5
      if BreakTime > 40:
        BreakTime = 40
      break
    Want_To_Eat = Food_List[random.randint(0,13)]
    Showing = {Food_List[random.randint(0,13)],Food_List[random.randint(0,13)],Want_To_Eat}
    print("")
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
