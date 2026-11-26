import time,random

Milk = {"StrawBerry Milk" : 800, 
        "Chocolate Milk" : 900, 
        "Banana Milk" : 700,
        "Coffee Milk" : 800,
        "Milk" : 600
    }

Milk_Stock = {
    "StrawBerry Milk" : random.randint(10,80),
    "Chocolate Milk" : random.randint(10,80),
    "Banana Milk" : random.randint(10,80),
    "Coffee Milk" : random.randint(10,80),
    "Milk" : random.randint(10,80),
    "name" : "milkstock"
}

Bread = {
    "Cream Bread" : 1000,
    "Red Bean Bread" : 900,
    "Sausage Bread" : 1200,
    "Salt Bread" : 1000,
    "White Bread" : 800,
    "Castella" : 900,
    "Scone" : 800,
    "Donut" : random.randrange(400,1000,100),
    }

Bread_Stock = {
    "Cream Bread" : random.randint(10,80),
    "Red Bean Bread" : random.randint(10,80),
    "Sausage Bread" : random.randint(10,80),
    "Salt Bread" : random.randint(10,80),
    "White Bread" : random.randint(10,80),
    "Castella" : random.randint(10,80),
    "Scone" : random.randint(10,80),
    "Donut" : random.randint(10,80),
    "name" : "breadstock"
}

Rice_Type_Food = {
    "Triangle Gimbap" : random.randrange(1400,2200,100),
    "Gimbap" : random.randrange(1800,2800,100),
    "Lunch Box" : random.randrange(3200,5000,100)
            }

Rice_Type_Food_Stock = {
    "Triangle Gimbap" : random.randint(10,80),
    "Gimbap" : random.randint(10,80),
    "Lunch Box" : random.randint(10,80),
    "name" : "ricetypefoodstock"
}

Snack ={
    "Potato Chip" : random.randrange(1800,2300,100),
    "Popcorn" : 1200,
    "Rice Chip" : 2200
    }

Snack_Stock = {
    "Potato Chip" : random.randint(10,80),
    "Popcorn" : random.randint(10,80),
    "Rice Chip": random.randint(10,80),
    "name" : "snackstock"
}

Beverage = {"Fruit Juice" : random.randrange(1200,2500,100),
            "Energy Drink" : random.randrange(1800,2800,100),
            "Soda" : random.randrange(1600,1900,100)
        }

Beverage_Stock = {
    "Fruit Juice" : random.randint(10,80),
    "Energy Drink" : random.randint(10,80),
    "Soda" : random.randint(10,80),
    "name" : "beveragestock"
}

Processed_Meat ={"Garlic Sausage" : 1600,
                 "Cheese Sausage" : 1500,
                 "Spicy Sausage" : 1700,
                 "Long Sausage" : 1800
            }

Processed_Meat_Stock = {
    "Garlic Sausage" : random.randint(10,80),
    "Cheese Sausage" : random.randint(10,80),
    "Spicy Sausage" : random.randint(10,80),
    "Long Sausage" : random.randint(10,80),
    "name" : "processedmeatstock"
}

Noodles = {"Cup Noodle" : random.randrange(900,2200,100),
           "Packed Noodle" : random.randrange(2000,4600,100)
        }

Noodles_Stock = {
    "Cup Noodle" : random.randint(10,80),
    "Packed Noodle" : random.randint(10,80),
    "name" : "noodlesstock"
}

Household_Item= {"Tissue" : 2300,
                 "Pencil" : 800,
                 "Eraser" : 600,
                 "Socks" : 1200,
                 "Portable Charger" : 6000,
                 "Charger" : 5500,
                 "Water Tissue" : 2500
            }

Household_Item_Stock = {
    "Tissue" : random.randint(10,80),
    "Pencil" : random.randint(10,80),
    "Eraser" : random.randint(10,80),
    "Socks" : random.randint(10,80),
    "Portable Charger" : random.randint(10,80),
    "Charger" : random.randint(10,80),
    "Water Tissue" : random.randint(10,80),
    "name" : "householditemstock"
}

Candy = {"Chocolate Bar" : random.randrange(1100,3000,100),
         "Lollipop" : 500,
         "Round Candy" : 400,
    } 

Candy_Stock = {
    "Chocolate Bar" : random.randint(10,80),
    "Lollipop" : random.randint(10,80),
    "Round Candy" : random.randint(10,80),
    "name" : "candystock"
}

IceCream = {"Hard Ice Cream" : random.randrange(1000,1800,100),
            "Pint Ice Cream" : random.randrange(4000,6000,100)
        }

IceCream_Stock = {
    "Hard Ice Cream" : random.randint(10,80),
    "Pint Ice Cream" : random.randint(10,80),
    "name" : "icecreamstock"
}

Instant_Cooking = {"Sawed Chicken" : 1800,
                   "Corn dog" : 1900,
                   "Cheese ball" : 600,
                   "Steamed Bread" : random.randrange(1600,2000,100)
                }

Instant_Cooking_Stock = {
    "Sawed Chicken" : random.randint(10,80),
    "Corn dog": random.randint(10,80),
    "Cheese ball" : random.randint(10,80),
    "Steamed Bread" : random.randint(10,80),
    "name" : "instantcookingstock"
}

Working_Time = 480
Earned_Money_Today = 0
Total_Collected_Money = 0
Day = 1
Convenience_Item_Big_List = [Milk,Bread,Rice_Type_Food,Snack,Beverage,Processed_Meat,Noodles,Household_Item,Candy,IceCream,Instant_Cooking]
Rating = 0
Customer_Good_Saying = ["This is the best Store ever in my life!","Thanks!","My Favorite","I'll come back later!","Great!","Nice!","Good!","Amzing"]
Customer_Bad_Saying = ["Why there are no","This is the worst Store EVER!","I'll never come back here","Is this your best?","I'll give low rating.."]

def Customer_Order():
    Amount_Decide = random.randint(0,100)
    Picked_Item_Amount_Decide = random.randint(0,100)
        
    if (Amount_Decide > 35) :
        Kind_Of_Item = 1
    elif (Amount_Decide > 30) :
        Kind_Of_Item = 2
    elif (Amount_Decide > 20) :
        Kind_Of_Item = 3
    elif (Amount_Decide > 10) :
        Kind_Of_Item = 4
    elif (Amount_Decide >= 0) :
        Kind_Of_Item = 5

    if (Picked_Item_Amount_Decide > 25):
        Picked_Item_Amount = 1 
    elif (Picked_Item_Amount_Decide > 10):
        Picked_Item_Amount = 2
    elif (Picked_Item_Amount_Decide > 5):
        Picked_Item_Amount = 3
    elif (Picked_Item_Amount_Decide >= 0):
        Picked_Item_Amount = 4
    
    Random_Int = random.randint(0,len(Convenience_Item_Big_List)-1)
    Picked_Item_Dictionary = Convenience_Item_Big_List[Random_Int]
    Picked_Item_Key_List = list(Picked_Item_Dictionary)
    
    Picked_Item = random.choice(Picked_Item_Key_List) #Choose one key from Item Category's Key List
    Picked_Item_Price = Picked_Item_Dictionary[Picked_Item]

    return Picked_Item ,Picked_Item_Price ,Picked_Item_Amount ,Kind_Of_Item ,Picked_Item_Dictionary

while True:
    print(f"Day : {Day}     Income : {Earned_Money_Today}       Total Income : {Total_Collected_Money}")
    if Working_Time // 60 > 12 and Working_Time > 7200:
         if Working_Time % 60 < 10:
                print(f"{Working_Time // 60} : 0{Working_Time % 60} PM")
         else:
            print(f"{Working_Time // 60} : {Working_Time % 60} PM")    
    elif Working_Time // 60 and Working_Time <= 7200:
        if Working_Time % 60 < 10:
            print(f"{Working_Time // 60} : 0{Working_Time % 60} AM")
        else:
            print(f"{Working_Time // 60} : {Working_Time % 60} AM")

    Ordered = Customer_Order()
    time.sleep(random.randint(1,5))
    print("(Customer Came.)")
    time.sleep(random.randint(5,8))
    print(f"Customer: Here ({Ordered[2]} {Ordered[0]}(s))")
    print(f"Price : {Ordered[1] * Ordered[2]}")
    calculated = 0
    while calculated < Ordered[2]:
        print(f"{calculated} / {Ordered[2]} ", end = '')
        User_Input = input("Calculating: ")
        if "name" in User_Input:
            print("yep")
            continue
        calculated += 1
        if calculated == Ordered[2]:
            print(f"{calculated} / {Ordered[2]} Calculated.")
    print("(Customer Left.)")
    Earned_Money_Today += Ordered[1] * Ordered[2]
    Working_Time += random.randrange(10,30,5)
    time.sleep(random.randint(5,15))   
    print(" ")


    