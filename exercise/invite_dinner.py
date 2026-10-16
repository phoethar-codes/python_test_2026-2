# make guest list and inviting
guest_list = ["Lucy", "Joe", "David"]
print(guest_list)
greeting = "Dear"
message = "Are you free tonight? I'd like to invite you to dinner.\nLet me know if you can make it!"
print(f"{greeting} {guest_list[0]}, \n{message}\n")
print(f"{greeting} {guest_list[1]}, \n{message}\n")
print(f"{greeting} {guest_list[2]}, \n{message}\n")

# changing guest list and invite again
absent_guest = guest_list[0]
guest_list[0] = "Ryan"
print(absent_guest)
print(guest_list)
print(f"{greeting} {guest_list[0]}, \n{message}\n")
print(f"{greeting} {guest_list[1]}, \n{message}\n")
print(f"{greeting} {guest_list[2]}, \n{message}\n")

# more 3 guests and  invite each person
guest_list.append("Rose")
guest_list.insert(0, "Hazel")
guest_list.insert(4, "Ella")
print(guest_list)
print(f"\n{greeting} {guest_list[0]}, \n{message}\n")
print(f"{greeting} {guest_list[1]}, \n{message}\n")
print(f"{greeting} {guest_list[2]}, \n{message}\n")
print(f"{greeting} {guest_list[3]}, \n{message}\n")
print(f"{greeting} {guest_list[4]}, \n{message}\n")
print(f"{greeting} {guest_list[5]}, \n{message}\n")

# shrinking guest list
print("I can invite only two people for dinner\n")
message = "I'm really sorry.I need to cancel our dinner plan."
print(f"{greeting} {guest_list.pop(0)}, \n{message}\n")
print(f"{greeting} {guest_list.pop(0)}, \n{message}\n")
print(f"{greeting} {guest_list.pop(0)}, \n{message}\n")
print(f"{greeting} {guest_list.pop(0)}, \n{message}\n")
greeting = "Hey"
message = "I'm stil inviting you to dinner"
print(f"{greeting} {guest_list[0]}! \n{message}\n")
print(f"{greeting} {guest_list[1]}! \n{message}\n")

del guest_list[0]
del guest_list[0]

print(guest_list)
