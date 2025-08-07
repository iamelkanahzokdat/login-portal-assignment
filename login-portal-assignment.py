verification_fee = 1500
users_db = []
user1 = {'name': 'red', 'password': '1234', 'balance': 20000.0, 'is_verified': True}
user2 = None
users_db.append(user1)

output = """
   *---------------------------------------*
   |      Login and Register Portal        |
   |   ________________________________    |
   |  commands:                            |
   |   enter "login" to login              |
   |   enter "register" to register        |
   *---------------------------------------*

"""
command = input(output).strip().lower()

if command not in ["login", "register"]:
    print("Invalid command")
    quit()

if command == "login":
    user_name = input("Enter your name:\n")
    password = input("Enter your Password: ")

    # Check first user
    if len(users_db) >= 1 and user_name == users_db[0]['name']:
        if password == users_db[0]['password']:
            print("Login successful!")
            print(users_db[0])
        else:
            print("Wrong password.")

    # Check second user
    elif len(users_db) >= 2 and user_name == users_db[1]['name']:
        if password == users_db[1]['password']:
            print("Login successful!")
            print(users_db[1])
        else:
            print("Wrong password.")

    else:
        print("Username not found. Please register.")
       

elif command == "register":
    user_name = input("Create a username: ")
    password = input("Create a password: ")
    balance = float(input("Enter balance: "))
