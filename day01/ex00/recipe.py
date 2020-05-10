class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if (not type(name) is str
                or not type(cooking_lvl) is int
                or not type(cooking_time) is int
                or not type(ingredients) is list
                or not type(description) is str
                or not type(recipe_type) is str
                or not 0 <= cooking_time
                or not 1 <= cooking_lvl <= 5
                or recipe_type not in ["starter", "lunch", "dessert"]):
            exit("ERROR")
        for arg in ingredients:
            if not type(arg) is str:
                exit("ERROR")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = ("- name: " + self.name + "\n" +
               "- cooking_lvl: " + str(self.cooking_lvl) + "\n" +
               "- cooking_time: " + str(self.cooking_time) + "\n" +
               "- ingredients: " + ", ".join(self.ingredients) + "\n" +
               "- description: " + self.description + "\n" +
               "- recipe_type: " + self.recipe_type)
        return txt

# empty인지는 아직 체크 못함.
# __str__과 str의 차이가 뭐지? __는 바로 실행되는 것인가?