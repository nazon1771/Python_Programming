import random,time
class Items:
  def __init__ (self,price,amount,name):
    self.price = price
    self.amount = amount
    self.name = name
class Boss_Fighting_Foods:
  def __init__ (self,dmg,add_anger,name):
    self.dmg = dmg
    self.add_anger = add_anger
    self.name = name
Exit_Condition = False
Anger_GameOver = False
Buying_Input =""
User_Input_Starting_Game =""
BreakTime = 15
Started_Games = 0
i = 0 #Counter for loop printing having foods
Food_List = ["Salad","Lemon","Banana","Strawberry","Apple","Donut","Vanilla Ice Cream","Cheese","Noodles","Soup","Potato","Fried egg","Orange","Glass of Milk","Grape","Watermelon","Pineapple","Mango","Cherry","Peach","Coconut"]
Donut = Boss_Fighting_Foods(-40,-4,"Donut")
Vanilla_Ice_Cream = Boss_Fighting_Foods(-30,-3,"Vanilla Ice Cream")
Mango = Boss_Fighting_Foods(-25,-3,"Mango")
Grape = Boss_Fighting_Foods(-20,-3,"Grape")
Apple = Boss_Fighting_Foods(-15,-2,"Apple")
Peach = Boss_Fighting_Foods(-10,-2,"Peach")
Sugary_Foods = [Donut, Vanilla_Ice_Cream, Mango, Grape, Apple, Peach]
Glass_of_Poison = Boss_Fighting_Foods(50,3,"Glass of Poison")
Pepper = Boss_Fighting_Foods(40,3,"Pepper")
Lemon = Boss_Fighting_Foods(30,2,"Lemon")
Hot_Noodles = Boss_Fighting_Foods(35,2,"Hot Noodles")
DMG_Foods = [Glass_of_Poison,Pepper,Lemon,Hot_Noodles]
Boss_Fight_Foods = set(DMG_Foods) | set(Sugary_Foods)
Boss_Fight_Foods_List = list(Boss_Fight_Foods)
Money = 0
anger = 0
Scissors = Items(300,0,"scissors")
Candy = Items(800,0,"candy")
Knife = Items(2000,0,"knife")
Radio = Items(400,0,"radio")
Card_Key = Items(5000,0,"card key")
Real_Want_To_Eat = "" #Means real food that Mr.tomato wants to eat
Showing_Want_To_Eat = "" #Means food that Mr.tomato wants to eat but it can be hidden by events
Showing = {} #Means You can choose food from this list to feed Mr.tomato, but it can be hidden by events 
Angry_Food_List = ["BRAIN","EYE","HAND"]
Int_Input = 0
Event_Sack = 0
Event_Mute = 0
Event_Mute_Starting_Rate = 0
Event_Starting_Rate = 0
Hiding1 = 0 #is used to print "(???)"
Hiding2 = 0
Used_Scissors = 0
Used_knife = 0
Used_Radio = 0
True_Ending = 0
Round_Initialized = False
Code_Name = random.randint(10000,99999)
Earned_Code = 0
User_Final_Decision = " "
Boss_HP = 200
Boss_Fighting_GameOver = False
Tomato_Boss_Death = False
#start
print("Welcome to the Game")
while Used_knife != 1 and Anger_GameOver != True and Boss_Fighting_GameOver != True and Tomato_Boss_Death != True:
  time.sleep(0.5)
  print("1.Shop")
  print("2.Game")
  print("3.Credit")
  print("4.How to play")
  print(f"Money: {Money}")
  if Earned_Code == 1:
    print(f"5.???")
  else:
    pass
  time.sleep(0.5)
  while True:
#User Menu input
    User_Input_Starting_Game = input("Where would you go? ").strip().lower()
    if User_Input_Starting_Game != "1" and User_Input_Starting_Game != "2" and User_Input_Starting_Game != "game" and User_Input_Starting_Game != "shop" and User_Input_Starting_Game != "3" and User_Input_Starting_Game != "credit":
      print(User_Input_Starting_Game)
      print("ENTER CORRECT NUMBER OF PLACE NAME")
      continue
    else:
      break    
#Credit
  if User_Input_Starting_Game == "3" or User_Input_Starting_Game == "credit":
      time.sleep(1)
      print("MADE BY nazon1771")
      print("(ft.Mimo,GitHub.dev)")
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
  if (User_Input_Starting_Game == "2" or User_Input_Starting_Game == "game") and Started_Games == 0:
    #Death after true ending
    if True_Ending == 1:
      time.sleep(10)
      print("Mr.tomato: I Said You Never Come Back,FOREVER")
      time.sleep(1)
      print("Mr.tomato: Why Did You Ignore Me?")
      time.sleep(1)
      print("Mr.tomato: I will make you pay for this")
      time.sleep(1)
      break
#IN game
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
    Started_Games += 1
  elif User_Input_Starting_Game == "2" and Started_Games != 0:
    print("Mr.tomato: Welcome Back.")
    print("")
    time.sleep(0.5)
    Started_Games += 1
#Playing Process  
  while User_Input_Starting_Game == "2":
      if not Round_Initialized:
        Real_Want_To_Eat = Food_List[random.randint(0,20)]#Real Having Foods Can't be changed
        Showing = {Food_List[random.randint(0,20)], Food_List[random.randint(0,20)]} #Showing foods can be hidden by events
        Showing.add(Real_Want_To_Eat)
        while len(Showing) < 3:
          Showing = {Food_List[random.randint(0,20)], Food_List[random.randint(0,20)]} #Showing foods can be hidden by events
          Showing.add(Real_Want_To_Eat)
        Showing_Want_To_Eat = (Real_Want_To_Eat + " ").strip() #Want to eat food can be hidden by events
        Showing_List = list(Showing) #Can be hidden by events
        Real_Having = list(Showing) #Can't be hidden by events
        Round_Initialized = True
      time.sleep(0.5)
      if Used_Radio == 1:
        print(f"I'd like to eat {Real_Want_To_Eat}")
        Used_Radio = 0
      else:
        print(f"I'd like to eat {Showing_Want_To_Eat}")
        Used_Radio = 0
      print(f"ANGER: {anger}")
      print(f"Left Food: {BreakTime}")
#Event Sack
      if Started_Games > 1 and Event_Sack == 1:
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
      if Started_Games > 1 and Event_Mute == 1:
        Showing_Want_To_Eat = "________"
      try:
        Giving = input("Enter Number or 'item'(To use items): ").strip().lower()
        if Giving == "item":
          print(f"Scissors: {Scissors.amount}")
          print(f"Candy: {Candy.amount}")
          print(f"Knife: {Knife.amount}")
          print(f"Radio: {Radio.amount}")
          Item_Using_Input = input("Which item would you use? ").strip().lower()
          if Item_Using_Input != "scissors" and Item_Using_Input != "candy" and Item_Using_Input != "knife" and Item_Using_Input != "radio":
            print("No Item Used")
            time.sleep(0.5)
            continue
#scissors event
          if Item_Using_Input == "scissors" and Scissors.amount > 0 and Started_Games > 0 and Event_Sack == 1:
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
#Radio event
          if Item_Using_Input == "radio" and Radio.amount > 0 and Event_Mute == 1:
            print("Used 'radio'")
            Radio.amount -= 1
            Used_Radio = 1
            continue
          elif Item_Using_Input == "radio" and Radio.amount == 0:
            print("You dont have radio")
            continue
        else:  
          Int_Input = int(Giving)
        if Int_Input > 3:
          print("Select numbers between 1~3")
          print("")
          continue
      except ValueError:
        print("Please enter 'Number'")
        continue  
      if Real_Having[Int_Input-1] == Real_Want_To_Eat:
        time.sleep(1)
        Money += 75
        BreakTime -= 1
        Event_Sack = 0
        Event_Mute = 0
        if Started_Games > 1:
          Event_Starting_Rate = random.randint(0,100)
          if Event_Starting_Rate > 65:
            Event_Sack = 1
        if Started_Games > 1:
          Event_Mute_Starting_Rate = random.randint(0,100)
          if Event_Mute_Starting_Rate > 75:
            Event_Mute = 1    
      else:
        time.sleep(1)
        print("Mr.tomato: I'd not asked This")
        Event_Sack = 0
        anger += 1
        BreakTime -= 1
        Money -= 75
      Round_Initialized = False
#GAME OVER
      if anger >= 10:
        print("Mr.tomato: YOU ARE THE WORST PERSON I HAVE EVER SEEN")
        time.sleep(1)
        print("Mr.tomato: DOING THIS SIMPLE WORK IS TOO HARD FOR YOU?")
        time.sleep(1)
        BreakTime = 10
        for i in range(1,11):
          print("Mr.tomato: Feed Me")
          print(f"Left Food: {BreakTime}")
          print(f"ANGER: {anger}")
          for i in range(1,4):
            print(f"{i}.{Angry_Food_List[i-1]}")
          try:
              Int_Input = int(input("Enter Number: "))
              if Int_Input > 3:
                print("Select numbers between 1~3")
                print("")
              BreakTime -= 1
              time.sleep(1)
              print("")
              if BreakTime == 0:
                print("Mr.tomato: OK,YOU DID A GREAT JOB")
                time.sleep(1)
                print("Mr.tomato: NOW, DIE")
                time.sleep(1)
                Anger_GameOver = True
                break
              continue
          except ValueError:
              print("Please enter 'Number'")
              time.sleep(1)
              continue
      if Started_Games == 8 and anger == 0 and BreakTime == 0:
              print("Mr.tomato: Wow,you were greater than I thought")
              time.sleep(1)
              print("Mr.tomato: I was surprised")
              time.sleep(1)
              print("Mr.tomato: I will give you a gift,a note that I couldn't understand")
              time.sleep(1) 
              print(f"NOTE: {Code_Name}")
              time.sleep(1)
              print("Mr.tomato: I think that you will understand it")
              time.sleep(1)
              print("Mr.tomato: Goodbye and don't come back never again")
              Earned_Code = 1
              continue
      if Started_Games == 8 and anger > 0 and BreakTime == 0:
              print("Mr.tomato: You Did A Great Job")
              time.sleep(1)
              print("Mr.tomato: I became Stronger than before")
              time.sleep(1)
              print("Mr.tomato: Now, You are USELESS")
              time.sleep(1)
              print("Mr.tomato: THEN..")
              time.sleep(2)
              print("Mr.tomato: DIE")
              anger = 0
              time.sleep(1)
              while Tomato_Boss_Death != True:
                print("FEED HIM!")
                print(f"Boss HP: {Boss_HP}")
                print(f"anger: {anger}")
                Boss_Fight_Foods_Shuffle = set(Boss_Fight_Foods)
                Boss_Fight_Foods_List = list(Boss_Fight_Foods_Shuffle)
                Sugary_Food_Amount = random.randint(1,2)
                DMG_Food_Amount = 3 - Sugary_Food_Amount
                Boss_Fight_Food_Showing = random.sample(Sugary_Foods, Sugary_Food_Amount) + random.sample(DMG_Foods, DMG_Food_Amount)
                for i in range(1,4):
                  print(f"{i}.{Boss_Fight_Food_Showing[i-1].name}")
                try:
                    Int_Input = int(input("Enter Number: "))
                    if Int_Input > 3:
                      print("Select numbers between 1~3")
                      print("")
                    if Boss_Fight_Food_Showing[Int_Input-1] == Glass_of_Poison:
                      anger += Glass_of_Poison.add_anger
                      Boss_HP -= Glass_of_Poison.dmg
                    elif Boss_Fight_Food_Showing[Int_Input-1] == Pepper:
                      anger += Pepper.add_anger
                      Boss_HP -= Pepper.dmg
                    elif Boss_Fight_Food_Showing[Int_Input-1] == Lemon:
                      anger += Lemon.add_anger
                      Boss_HP -= Lemon.dmg
                    elif Boss_Fight_Food_Showing[Int_Input-1] == Hot_Noodles:
                      anger += Hot_Noodles.add_anger
                      Boss_HP -= Hot_Noodles.dmg
                    elif Boss_Fight_Food_Showing[Int_Input-1] == Donut:
                      anger += Donut.add_anger
                      Boss_HP -= Donut.dmg
                    elif Boss_Fight_Food_Showing[Int_Input-1] == Vanilla_Ice_Cream:
                      anger += Vanilla_Ice_Cream.add_anger
                      Boss_HP -= Vanilla_Ice_Cream.dmg
                    elif Boss_Fight_Food_Showing[Int_Input-1] == Mango:
                      anger += Mango.add_anger
                      Boss_HP -= Mango.dmg
                    elif Boss_Fight_Food_Showing[Int_Input-1] == Grape:
                      anger += Grape.add_anger
                      Boss_HP -= Grape.dmg
                    elif Boss_Fight_Food_Showing[Int_Input-1] == Apple:
                      anger += Apple.add_anger
                      Boss_HP -= Apple.dmg
                    elif Boss_Fight_Food_Showing[Int_Input-1] == Peach:
                      anger += Peach.add_anger
                      Boss_HP -= Peach.dmg
                    print(f"You Fed {Boss_Fight_Food_Showing[Int_Input-1].name}!")
                    time.sleep(0.5)
                    print(" ")
                    time.sleep(0.5)
                    if anger < 0:
                      anger = 0
                    if Boss_HP >= 200:
                      Boss_HP = 200
                    if anger >= 10 and Boss_HP > 0:
                      print("Mr.tomato: BYE")
                      Boss_Fighting_GameOver = True
                      time.sleep(1)
                      break
                    if Boss_HP <= 0:
                      print("Mr.tomato: ...")
                      time.sleep(1)
                      print("Mr.tomato: You won")
                      Tomato_Boss_Death = True
                      break
                except ValueError:
                    print("Please enter 'Number'")
                    time.sleep(1)
                    continue          
#BREAK TIME
      if BreakTime == 0 or BreakTime < 0:
        if Tomato_Boss_Death == True or Anger_GameOver == True or Boss_Fighting_GameOver == True:
          break
        time.sleep(0.5)
        print("Mr.tomato: Ok,I'm full for now")
        time.sleep(1)
        print("Mr.tomato: Come back later if I become hungry")
        time.sleep(2)
        print("Mr.tomato: See you later")
        BreakTime = 15 + Started_Games * 5
        if BreakTime > 40:
          BreakTime = 40
        break
      Want_To_Eat = Food_List[random.randint(0,20)]
      Showing = {Food_List[random.randint(0,20)],Food_List[random.randint(0,20)],Want_To_Eat}
      print("")
      #SHOPPING
  while User_Input_Starting_Game == "1" or User_Input_Starting_Game == "shop":
    if Exit_Condition == False:
      print("--------SHOP--------")
      print(f"Scissors: {Scissors.price}, you have {Scissors.amount} scissor(s)")
      print(f"Candy: {Candy.price}, you have {Candy.amount} candy(s)")
      print(f"Knife: {Knife.price}, you have {Knife.amount} knife")
      print(f"Radio: {Radio.price}, you have {Radio.amount} radio")
      if Card_Key.amount == 1:
        print(f"You have a card key")
      else:
        print(f"???: {Card_Key.price}")
      print("1.Scissors")
      print("2.Candy")
      print("3.Knife")
      print("4.Radio")
      if Card_Key.amount == 1:
        print("5.Card Key")
      else:
        print("5.???")
      print("6.exit")
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
            continue
          Money -= Knife.price
          Knife.amount += 1
          print("Purchased 'Knife'!")
          print("")
        else:
          print("You don't have enough money")
          print("")
      elif Buying_Input == "4":
        if Money >= Radio.price:
          Money -= Radio.price
          Radio.amount += 1
          print("Purchased 'Radio'!")
          print("")
        else:
          print("You don't have enough money")
          print("")
      elif Buying_Input == "5":
        if Money >= Card_Key.price:
          Money -= Card_Key.price
          Card_Key.amount += 1
          print("Purchased 'Card Key'!")
          print("")
        else:
          print("You don't have enough money")
          print("")
      if Buying_Input == "6":
          Exit_Condition = True
    elif Exit_Condition == True:
      Exit_Condition = False
      break
  while User_Input_Starting_Game == "5" and Earned_Code == 1:
    print("--------???--------")
    print("1.DELETE")
    print("2.SAVE")
    User_Final_Decision = input("WHAT WOULD YOU DO? ").strip().lower()
    if User_Final_Decision == "1":
      time.sleep(2)
      if Card_Key.amount == 1:
        time.sleep(2)
        print("DELETEING DATA ...")
        time.sleep(2)
        print("Mr.tomato: WAIT, WHAT ARE YOU DOING?!")
        time.sleep(1)
        print("Mr.tomato: ...You were smarter than I thought")
        time.sleep(1)
        print("Mr.tomato: ..YOU WON")
        break
      elif Card_Key.amount == 0:
        time.sleep(3)
        print("Mr.tomato: DO YOU THINK THAT YOU WON ME?")
        time.sleep(1)
        print("Mr.tomato: YOU WERE SILLIER THAN I THOUGHT")
        time.sleep(1)
        print("Mr.tomato: I'M GOD FROM NOW")
        time.sleep(1)
        print("Mr.tomato: DIE")
        break