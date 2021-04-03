
class book:
    recipes_list={"starter":" ","lunch": " ","desert":" ",}
    name="0"
    last_update="0"
    creation_date="0"
    def __str__(self,name,last_update,creation_date,recipes_list):
        self.name = name
        self.last_update = last_update 
        self.creation_date = creation_date
        self.recipes_list = recipes_list
        
    def get_recipe_by_name(self, name):
        pass
        for key in self.recipes_list:
            for recipe in self.recipes_list[key]:
                if recipe.name==name:
                    print(recipe)
                
        

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
