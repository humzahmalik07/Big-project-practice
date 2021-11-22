def first_note():
  filename = 'user.txt'
  character = input("What do you want to note today? ")
  with open(filename, 'w') as file_object:
    file_object.write(character)
  filename_2 = open("user.txt", "r")
  print(filename_2.read())
  
def first_note_add():
  filename = 'user.txt'
  add_note = input("Do you want to add more? ")
  if add_note == "yes":
    add = input("What do you want to add:\n")
    with open(filename, 'a') as file_object:
      file_object.write(add)
    filename_3 = open("user.txt", "r")
    print(filename_3.read())
  if add_note == "no":
    quit()  

def main_menu():
    print(""" Hi!, Welcome to the Notes Program 
    
  In this program, you will be able to create, edit and delete notes.
  
  You will be allowed maximum 10 notes on this program. 
  
  *Notes*: Press space at the start when editing an existing file. 
           Press enter to start a new line""")
    print("\n")

valid_actions = ["create a file", "edit a file", "delete a file", "Close the program"]

def menu():
        """ Prints out the menu for all the possible actions
        taken by the user """
        print("""Choose an action:
    """)
        for input in valid_actions:
            print(f"* {input}")



def intro():
  print(input("What would you like to do today? "))


main_menu()
menu()
intro()
first_note()
first_note_add()
