# Import the string module to access punctuation characters
import string

# Import everything from pyscript to allow interaction with the DOM
from pyscript import *

def password_checkerv1():
    # ---- USERNAME CHECKS ----

    # Check if username is at least 7 characters long
    if len(document.getElementById("username_inp").value) < 7:
        return "Username not long enough"
    else:
        # Check if username is NOT only letters
        if not document.getElementById("username_inp").value.isalpha():
            # Check if username is NOT only digits
            if not document.getElementById("username_inp").value.isdigit():
                # Username contains both letters and digits → valid
                print("Valid")
            else:
                # Username has only digits
                return "Please include letters on your username"
        else:
            # Username has only letters
            return "Please include digits on your username"

    # ---- PASSWORD CHECKS ----

    # Get the password input value
    pass_grab = document.getElementById("password_inp").value

    # Loop through each character in the password
    for char in pass_grab:
        # Check if the password contains special characters
        if char in list(string.punctuation):
            return "No Special Characters on your password"

    # Check if password is at least 10 characters long
    if len(pass_grab) < 10:
        return "Password not long enough"

    # Check if password is NOT only letters
    if not pass_grab.isalpha():
        # Check if password is NOT only digits
        if not pass_grab.isdigit():
            # Password contains both letters and digits → valid
            return True
        else:
            # Password has only digits
            return "Please include letters on your password"
    else:
        # Password has only letters
        return "Please include digits on your password"


def check_pass(e):
    # Clear previous output message
    document.getElementById("output").innerHTML = ""

    # Run the password and username checker
    result = password_checkerv1()

    # If validation passed
    if result == True:
        document.getElementById("output").style.color = "green"
        document.getElementById("output").innerHTML = (
            f"Your account is valid. Welcome, "
            f"{document.getElementById('username_inp').value}"
        )
    else:
        # If validation failed, show error message
        document.getElementById("output").style.color = "red"
        document.getElementById("output").innerHTML = result
