import gooeypie as gp
import pyhibp
from pyhibp import pwnedpasswords as pw

# Useful emoji
checkbox_true = "✅"
checkbox_false = "❌"

# Create the GooeyPie app
app = gp.GooeyPieApp('BOSSBREAK')
app.width = 500
app.height = 500
app.title = "BOSSBREAK"

# Create GUI elements
password_label = gp.Label(app, " Please Type in Password")
password_input = gp.Secret(app)
password_input.width = 50

show_password_checkbox = gp.Checkbox(app, 'Show password')
status_label = gp.Label(app, '')

len_lbl = gp.Label(app, '')
case_lbl = gp.Label(app, '')

# Function to check the password length (8-16 characters)
def check_len(password):
    if len(password) < 8:
        len_lbl.text = f"{checkbox_false} Password is too short, minimum 8 characters."
    elif len(password) > 16:
        len_lbl.text = f"{checkbox_false} Password is too long, maximum 16 characters."
    else:
        len_lbl.text = f"{checkbox_true} Password length is good."

# Function to check if password has both lowercase and uppercase letters
def check_case(password):
    has_lower = False
    has_upper = False
    
    for char in password:
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True
    
    if not has_lower:
        case_lbl.text = f"{checkbox_false} Password must contain lowercase letters."
    elif not has_upper:
        case_lbl.text = f"{checkbox_false} Password must contain uppercase letters."
    else:
        case_lbl.text = f"{checkbox_true} Password has both uppercase and lowercase letters."

# Function to check for at least one special character
def check_symbol(password):
    symbols = "!@#$%^&*()-_+=<>?{}[]|\\/.:,;\"'`~"
    if any(char in symbols for char in password):
        return True
    return False

# Function to check the password strength
def check_password(event):
    password = password_input.text
    errors = []

    check_len(password)
    check_case(password)

    if not check_symbol(password):
        errors.append(f"{checkbox_false} Password must contain at least one special character.")

    # Display errors or success message
    if errors:
        status_label.text = "\n".join(errors)
    else:
        status_label.text = "Password is strong."

def check_if_breached(password):
    # API request to check if password has been breached
    pyhibp.set_user_agent(ua="BossBreakChecker/0.1 (Checker)")

    resp = pw.is_password_breached(password=password)
    if resp:
        case_lbl.text("Password breached!")
        case_lbl.text("This password was used {0} time(s) before.".format(resp))
        return False
    else:
        return True
        case_lbl.text("This password has never been breached")


# Function to toggle the visibility of the password
def toggle_password_visibility(event):
    password_input.toggle()

# Create the 'Check' button
check_button = gp.Button(app, 'Check', check_password)
show_password_checkbox.add_event_listener('change', toggle_password_visibility)

# Set grid layout
app.set_grid(7, 1)
app.add(password_label, 1, 1)
app.add(password_input, 2, 1)
app.add(show_password_checkbox, 3, 1)
app.add(check_button, 4, 1)
app.add(status_label, 5, 1)
app.add(len_lbl, 6, 1)
app.add(case_lbl, 7, 1)

# Run the app
app.run()
