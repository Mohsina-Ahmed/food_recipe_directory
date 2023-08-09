class Recipes:
    def __init__(self, id, name, time, rate):
        self.id = id
        self.name = name
        self.cooking_time = time
        self.rating = rate

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Recipes({self.id}, {self.name}, {self.cooking_time}, {self.rating})"
