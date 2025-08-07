"""
ASSIGNMENT: Login and Registration Portal System

OBJECTIVE:
Create a simple command-line user management system that allows/prompts users to register new accounts, 
login to existing accounts, and optionally verify their accounts for a fee.

REQUIREMENTS:

1. SYSTEM SETUP:
   - Create a verification cost of 1500 (stored in a variable)
   - Initialize an empty variable "users_db" to store user data for all users
   - Display a welcome portal with clear instructions (provided in code below)

2. MAIN MENU:
   - Present users with a formatted welcome message showing available commands
   - Accept user input for either "login" or "register" (case-insensitive)
   - Handle invalid commands with appropriate error messages

3. REGISTRATION FUNCTIONALITY:
   - Prompt user for username, password, and initial balance
   - Check if username already exists in "users_db" (prevent duplicates)
   - Store new user with the following data structure:
     * username (string)
     * password (string)
     * balance (float)
     * is_verified (boolean, default: False)
   - Display success message and user information after creation

4. VERIFICATION SYSTEM (Post-Registration):
   - After successful registration, offer optional account verification
   - Show verification cost and prompt user for yes/no decision
   - If user chooses "yes":
     * Check if user has sufficient balance
     * If sufficient: deduct verification cost and set is_verified to True
     * If insufficient: display error message with current balance and required amount
   - Regardless of verification choice (whether the user wishes to verify or not), display "Login successful!" and user info

5. LOGIN FUNCTIONALITY:
   - Prompt user for username and password
   - Validate that username exists in the system
   - Verify password matches stored password
   - Display appropriate success or error messages:
     * Success: "login successful!" + user information
     * Username not found: f"user {username} does not exists"
     * Wrong password: f"password mismatch for {username}"

6. DATA STRUCTURE:
   Each user should have the following details:

"""
   #TODO: Implement the login and registration portal system based on the requirements above

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
                user2['is_verified'] = True
                print("Account verified successfully.")
                print(user2)
            else:
                print(f"Insufficient balance. You have NGN{user1['balance']} but NGN1500 is required.")

        if verify == "no":
            if user1['balance'] >= verification_fee:
                user1['is_verified'] = False
                print("Login Successfull")
                print(user2)
        
            else:
               if verify not in ["verify"]:
                  print("Invalid command.")
                  quit()
