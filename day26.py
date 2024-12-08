num = []
for i in range(0,100):
    print(num)

food = input("enter fav food:")
food1 = input("enter fav food1:")
food2 = input("enter fav food2:")
food3 = input("enter fav food3:")
foods = [food,food1,food2,food3]
foods.pop(-1)
print(foods)

name = input("enter name")
if len(name)[6]:
    print ("hello")
elif len(name)[5]:
    print ("ola")
elif len(name)[6<name]:
    print("bonju")

food_list = ["Pizza", "Burger", "Pasta", "Salad", "Sushi"]

favorite_food = input("შეიყვანეთ თქვენი საყვარელი საჭმელი: ")
index = int(input("რომელ ინდექსზე ჩასვათ (0-დან 4-მდე): "))

if 0 <= index < len(food_list):
    food_list[index] = favorite_food  
    print("განახლებული სია:", food_list)
else:
    print("არასწორი ინდექსი!")
