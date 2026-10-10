name = "eric"  # practice string methods
print(f"Hello {name.upper()}, would you like to learn some Python today?")
name = "ETIC"
print(f"hello {name.lower()}, would you like to learn some Python today?")
text = "hello Eric, would you like to learn some python today?"
print(text.title())
print("Mahatama Gandhi once said, \"Live as if you were to die tomorrow, \nlearn as if you were to live forever.\"")
famous_person = "Mahatama Gandhi"
quote = "\"Live as if you were to die tomorrow, \nlearn as if you were to live forever.\""
message = f"{famous_person} once said, {quote}"
print(message)
print("\n\t\t\"Live as if you were to die tomorrow,\n\t\tlearn as if you were to live forever.\"\n\t\t\t\'Mahatama Gandhi\'")
name = "\t\tMahatama Gandhi\t\t"
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())
file = "python_note.txt"
print(file.removeprefix("python"))
print(file.removesuffix("txt"))
