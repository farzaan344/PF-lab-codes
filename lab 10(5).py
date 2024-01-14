print("Farzaan Bin Khawar\n2023F-BIT-030")
initial_menu = ("Biryani", "Nalli nihari", "Beef pulao", "Salad", "Doodh Dulaari")

print("Initial Menu:")
for food in initial_menu:
    print(food)

new_menu = list(initial_menu)
new_menu[0] = "Mutton Mandi"
new_menu[2] = "Brown karahi"

updated_menu = tuple(new_menu)

print("\nUpdated Menu:")
for food in updated_menu:
    print(food)
