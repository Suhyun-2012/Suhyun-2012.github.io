from random import *

Appetizer = [ "chips", "eggs", "soup", "cheese", "bread", "salad" ]
Meal = [ "burger", "pasta", "sushi", "ribs", "steak", "skewers", "pork chops", "vegan wrap" ]
Dessert = [ "ice cream", "banana split", "fruit salad", "cake", "cookies", "patbingsu" ]

Food = input( "What do you want to eat?")

num1 = randint(0, len(Appetizer)-1)
num2 = randint(0, len(Meal)-1)
num3 = randint(0, len(Dessert)-1)

if(input !="I dont know"):
    print( "You are having...")
    print(Appetizer[num1]+" "+Meal[num2]+" "+Dessert[num3])
else:
    print( "get out" )
