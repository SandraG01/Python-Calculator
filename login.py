realuser = ["Anthony", "Sandra"]
realpassword = "very difficult password"

username = input("Enter username: ")
password = input ("Enter password: ")

if username in realuser or realpassword == password:
    print(f"{username} logged in")
else:
    print("incorrect")