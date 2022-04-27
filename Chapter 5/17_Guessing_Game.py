password = "mywife"
guess = ""
guess_limit = 3
guess_count = 0
out_of_guess = False

while guess != password and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("Enter the password: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Incorrect password! Your account has been locked.")
else:
    print("You have logged in successfully.")