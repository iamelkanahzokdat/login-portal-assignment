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
    is_verified = False

    if len(users_db) > 0 and users_db[0]['name'] == user_name:
        print("Username exists already")
    else:
        user2 = {
            'name': user_name,
            'password': password,
            'balance': balance,
            'is_verified': is_verified
        }
        users_db.append(user2)
        print("Registration successful!")
        print(user2)

        # Verification prompt only after registration
        verify = input("Would you like to verify your account for NGN1500? (yes/no): ").strip().lower()
        verification_fee = 15000
        if verify == "yes":
            if user1['balance'] >= verification_fee:
                user1['balance'] -= verification_fee
                user1['is_verified'] = True
                print("Account verified successfully.")
                print(user)
            else:
                print(f"Insufficient balance. You have NGN{user['balance']} but NGN1500 is required.")

        if verify == "no":
            if user1['balance'] >= verification_fee:
                user1['is_verified'] = False
                print("Login Successfull")
                print(user1)
        
            else:
               if verify not in ["verify"]:
                  print("Invalid command.")
                  quit()


