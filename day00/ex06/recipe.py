dict = {
    "sandwich" : {
        "ingredients" : ["ham", "bread", "cheese"],
        "meal" : "lunch",
        "prep_time" : "10 minutes"
    },
    "cake" : {
        "ingredients" : ["flour", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time" : "60 minutes"
    },
    "salad" : {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : "15 minutes"
    }
}

## 딕셔너리 value, key 리스트 만들기
# print(sandwich.keys())
# print(sandwich.values())
# print(list(sandwich.keys()))
# print(list(sandwich.values()))

def print_recipe(input):
    if input in dict:
        print()
        print("Recipe for {}:".format(input))
        print("Ingredients list: {}".format(dict[input]["ingredients"]))
        print("To be eaten for {}.".format(dict[input]["meal"]))
        print("Takes {} of cooking.".format(dict[input]["prep_time"]))
    else:
        print("{} is not in cookbook.".format(input))

def del_recipe(input):
    del dict[input]

def add_recipe(name, ingredients, meal, prep_time):
    dict[name] = {
        "ingredients" : ingredients,
        "meal" : meal,
        "prep_time" : prep_time
    }

def print_cookbook():
    for i in range(len(dict)):
        print_recipe(list(dict)[i])

explane_num = '''Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit'''
print(explane_num)

n = ""
while n != "5":
    n = input(">> ")
    if n == "1":
        name = input("\nPlease enter the name of recipe.\n>> ")
        ingredients = input("\nPlease enter the gredients of recipe.\nex) ['flour', 'sugar', 'eggs']\n>> ")
        meal = input("\nPlease enter type of meal.\n>> ")
        prep_time = input("\nPlease enter the prep_time.\nex) 15 minute\n>> ")
        add_recipe(name, ingredients, meal, prep_time)
    elif n == "2":
        name = input("\nPlease enter the name of recipe to delete.\n>> ")
        del_recipe(name)
    elif n == "3":
        x = input("\nPlease enter the recipe's name to get its details:\n>> ")
        print_recipe(x)
    elif n == "4":
        print_cookbook()
    elif n == "5":
        print("\nCookbook closed.")
        exit()
    else:
        print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter 5.")
