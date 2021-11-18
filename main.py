file = open("practice.txt", "r")
print(file.read())

file_2 = open("practice.txt", "w")

filename = 'user.txt'
character = input("What is your character's name? ")
with open(filename, 'w') as file_object:
    file_object.write(character)
    
filename_2 = open("user.txt", "r")
print(filename_2.read())