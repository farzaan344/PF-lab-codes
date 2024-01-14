print("Farzaan Bin Khawar\n2023F-BIT-030")
dinner_guests = ["Tahreem", "Shazil", "Hafsa", "Gull", "Irtiza 50% CR", "Irtiza Singer", "Khizer", "Aleeza the delulu"]
print("Initial Invitations:")
for guest in dinner_guests:
    print(f"Dear {guest}, you are invited to dinner.")
unavailable_guest = "Irtiza 50% CR"
if unavailable_guest in dinner_guests:
    del dinner_guests[dinner_guests.index(unavailable_guest)]
    new_guest = "Zaid half CR"
    dinner_guests.insert(dinner_guests.index("Tahreem"), new_guest)
print("\nUpdated Invitations:")
for guest in dinner_guests:
    print(f"Dear {guest}, you are invited to dinner.")
