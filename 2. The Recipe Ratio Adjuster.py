#Task 1: Start

def get_number_of_servings(prompt):
    while True:
        try:
            servings = int(input(prompt))
            if servings <= 0:
                raise ValueError("Number of servings must be a positive integer.")
            return servings
        except ValueError as ve:
            print(f"Error: {ve}. Please enter a valid number of servings.")

original_servings = get_number_of_servings("Enter the number of servings the recipe is originally for: ")
desired_servings = get_number_of_servings("Enter the number of servings you wish to make: ")

print("Original servings:", original_servings)
print("Desired servings:", desired_servings)

#Task 2: Quantity Calculation

def get_number_of_servings(prompt):
    while True:
        try:
            servings = int(input(prompt))
            if servings <= 0:
                raise ValueError("Number of servings must be a positive integer.")
            return servings
        except ValueError as ve:
            print(f"Error: {ve}. Please enter a valid number of servings.")

def calculate_adjustment_factor(original_servings, desired_servings):
    try:
        adjustment_factor = desired_servings / original_servings
        return adjustment_factor
    except ZeroDivisionError:
        print("Error: Original servings cannot be zero.")
        return None
    except ArithmeticError as ae:
        print(f"Arithmetic error occurred: {ae}")
        return None

original_servings = get_number_of_servings("Enter the number of servings the recipe is originally for: ")
desired_servings = get_number_of_servings("Enter the number of servings you wish to make: ")

adjustment_factor = calculate_adjustment_factor(original_servings, desired_servings)

if adjustment_factor is not None:
    print("Adjustment factor:", adjustment_factor)

#Task 3: Serving Success

def get_number_of_servings(prompt):
    while True:
        try:
            servings = int(input(prompt))
            if servings <= 0:
                raise ValueError("Number of servings must be a positive integer.")
            return servings
        except ValueError as ve:
            print(f"Error: {ve}. Please enter a valid number of servings.")

def calculate_adjustment_factor(original_servings, desired_servings):
    try:
        adjustment_factor = desired_servings / original_servings
        return adjustment_factor
    except ZeroDivisionError:
        print("Error: Original servings cannot be zero.")
        return None
    except ArithmeticError as ae:
        print(f"Arithmetic error occurred: {ae}")
        return None

def adjust_recipe_quantities(recipe, adjustment_factor):
    adjusted_recipe = {}
    for ingredient, quantity in recipe.items():
        adjusted_recipe[ingredient] = quantity * adjustment_factor
    return adjusted_recipe

original_servings = get_number_of_servings("Enter the number of servings the recipe is originally for: ")
desired_servings = get_number_of_servings("Enter the number of servings you wish to make: ")

adjustment_factor = calculate_adjustment_factor(original_servings, desired_servings)

if adjustment_factor is not None:
    print("Adjustment factor:", adjustment_factor)
    # Define your recipe dictionary here with ingredient quantities
    recipe = {"Ingredient1": 100, "Ingredient2": 200, "Ingredient3": 300}  # Example recipe
    adjusted_recipe = adjust_recipe_quantities(recipe, adjustment_factor)
    print("Adjusted Recipe Quantities:")
    for ingredient, quantity in adjusted_recipe.items():
        print(f"{ingredient}: {quantity} units")

try:
    print("Enjoy your cooking!")
finally:
    print("Thank you for using the recipe adjustment tool.")