def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('hamster','harry')
pet={'animal_type':'hamster','pet_name':'harry'}
pet_def=[]
for value in pet.values():
    pet_def.append(value)

print(pet_def)


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg="Hello, "+name.title()+"!"
        print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)
