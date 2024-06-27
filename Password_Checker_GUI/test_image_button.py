import gooeypie as gp
import pyhibp
from pyhibp import pwnedpasswords as pw
import pyperclip

# Required: A descriptive user agent must be set describing the application consuming the HIBP API
pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")

# Create the main application window
app = gp.GooeyPieApp('BOSSBREAK')

# Create the help window
help_window = gp.Window(app, 'Help')
help_window.set_grid(3, 1)
help_text = gp.Label(help_window, 'BOSSBREAK, designed and developed by Harrison Dearing, provides a strength assessment of your password. It includes the following features:\n'
                                 '- Password Length: Longer passwords are stronger and more effective.\n'
                                 '- Password Complexity: Mix of upper and lower case letters, numbers, and special characters.')
help_window.add(help_text, 1, 1, align='center')

# Create the about window
about_window = gp.Window(app, 'About')
about_window.set_grid(1, 1)
about_text = gp.Label(about_window, 'BOSSBREAK - An innovative tool for assessing password strength.')
about_window.add(about_text, 1, 1, align='center')

# Set app properties
app.set_grid(12, 3)
app.width = 600
app.height = 400
app.title = 'BOSSBREAK'

# Create UI components
password_input = gp.Secret(app, 'Enter Password')
len_lbl = gp.Label(app, '')
case_lbl = gp.Label(app, '')
num_lbl = gp.Label(app, '')
special_lbl = gp.Label(app, '')
score_lbl = gp.Label(app, '')
breach_lbl = gp.Label(app, '')
status_lbl = gp.Label(app, '')

def check_password_strength(event):
    password = password_input.text
    score = 0

    # Check password length
    if len(password) < 12:
        len_lbl.text = 'Password is too short, minimum 12 characters'
        score += 10
    elif len(password) > 16:
        len_lbl.text = 'Password is too long, maximum 16 characters'
        score += 5
    else:
        len_lbl.text = 'Password length is good'
        score += 20

    # Check for uppercase and lowercase characters
    if password.islower():
        case_lbl.text = 'Password is all lowercase, add uppercase letters'
        score += 5
    elif password.isupper():
        case_lbl.text = 'Password is all uppercase, add lowercase letters'
        score += 5
    else:
        case_lbl.text = 'Password has mixed case characters'
        score += 20

    # Check for numbers
    if any(char.isdigit() for char in password):
        num_lbl.text = 'Password contains numbers'
        score += 20
    else:
        num_lbl.text = 'Password should contain at least one number'
        score += 5

    # Check for special characters
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    if any(char in special_chars for char in password):
        special_lbl.text = 'Password contains special characters'
        score += 20
    else:
        special_lbl.text = 'Password should contain at least one special character'
        score += 5

    # Check for repeated characters
    if len(password) != len(set(password)):
        score += 10

    # Calculate and display the score
    score_lbl.text = f'Your password score is {score}'

    # Check if the password has been breached
    resp = pw.is_password_breached(password=password)
    if resp:
        breach_lbl.text = f'Password breached! This password was used {resp} time(s) before.'
    else:
        breach_lbl.text = 'Password not found in breach database.'

def toggle_password_visibility(event):
    password_input.secret = not password_input.secret
    show_password_btn.text = 'Hide Password' if not password_input.secret else 'Show Password'

def open_help_window(event):
    help_window.show()

def open_about_window(event):
    about_window.show()

def copy_to_clipboard(event):
    pyperclip.copy(password_input.text)
    status_lbl.text = "Text copied to clipboard!"

# Create buttons and add event listeners
check_btn = gp.Button(app, 'Check Password Strength', check_password_strength)
show_password_btn = gp.Button(app, 'Show Password', toggle_password_visibility)
help_btn = gp.Button(app, 'Help', open_help_window)
about_btn = gp.Button(app, 'About', open_about_window)
copy_btn = gp.Button(app, 'Copy to Clipboard', copy_to_clipboard)

# Arrange components in the grid
app.add(password_input, 1, 1, colspan=2)
app.add(show_password_btn, 1, 3)
app.add(check_btn, 2, 1, colspan=3)
app.add(len_lbl, 3, 1, colspan=3)
app.add(case_lbl, 4, 1, colspan=3)
app.add(num_lbl, 5, 1, colspan=3)
app.add(special_lbl, 6, 1, colspan=3)
app.add(score_lbl, 7, 1, colspan=3)
app.add(breach_lbl, 8, 1, colspan=3)
app.add(help_btn, 9, 1)
app.add(about_btn, 9, 2)
app.add(copy_btn, 9, 3)
app.add(status_lbl, 10, 1, colspan=3)

app.run()
