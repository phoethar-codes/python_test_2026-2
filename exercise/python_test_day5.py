# make a list
my_friends = ["Khaing Wint Maw", "Zin Mon", "Htet May Oo", "Khaing Pan Zone"]
# print each person's name
print(my_friends[0])
print(my_friends[1])
print(my_friends[2])
print(my_friends[3])
# make a message
message = "\"Hello! What's up.\""
# print a message to them
print(message)
print(f"{message}{my_friends[2]}")
print(f"{message}{my_friends[3]}")
# make a list favourite transportation
fav_transport = ["motorcycle", "car", "bicycle"]
# make a message and print
message = "I would like to own a "
print(f"{message}{fav_transport[0]}")
print(f"{message}{fav_transport[1]}")
# .append methods
motorcycles = ["Honda", "Suzuki", "Ducati"]
print(motorcycles)
motorcycles.append("Yamaha")
print(motorcycles)
motorcycles[0] = "BMW"
print(motorcycles)
motorcycles.append("Honda")
print(motorcycles)
motorcycles.insert(1, "Harley")
print(motorcycles)
del motorcycles[0]
print(motorcycles)
ported_motorcycles = motorcycles.pop()
print(motorcycles)
print(ported_motorcycles)
motorcycles.remove("Yamaha")
print(motorcycles)
