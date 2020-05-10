class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        if (type(name) is not str
            or type(last_update) is not datetime
            or type(creation_date) is not datetime
            or type(recipes_list) is not dict
            or recipes_list not in ["starter", "lunch", "dessert"]):
            exit("ERROR")
        