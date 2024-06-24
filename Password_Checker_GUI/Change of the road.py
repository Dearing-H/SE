import gooeypie as gp

# Create the main application window
app = gp.GooeyPieApp('BOSSBREAK')

# Create the second window (Help)
help_window = gp.Window(app, 'Help')
help_window.width = 400
help_window.height = 300
help_window.set_grid(3, 1)
help_text = gp.Label(help_window, 'BOSSBREAK Designed and Developed by Harrison Dearing is a program that is designed to provide you with the strength level of your password. BOSSBREAK has been released using a GUI public license, currently equipped with the following features:\n\n- Password Length: Longer passwords are stronger and more effective, choose between 10, 12, and 14\n- Password Complexity: Mix of characters.')
help_window.add(help_text, 1, 1, align='center')

# Create the third window (About)
about_window = gp.Window(app, 'About')
about_window.width = 400
about_window.height = 300
about_window.set_grid(3, 1)
about_text = gp.Label(about_window, 'This program was created by Harrison Dearing to help users assess the strength of their passwords. It is released under the GUI public license and aims to encourage strong password practices.')
about_window.add(about_text, 1, 1, align='center')

# Set app properties
app.width = 600
app.height = 300
app.title = "BOSSBREAK"

# Create UI components
password_input = gp.Secret(app)
confirm_password_input = gp.Secret(app)
len_lbl = gp.Label(app, '')
num_lbl = gp.Label(app, '')
lowercase_lbl = gp.Label(app, '')
uppercase_lbl = gp.Label(app, '')
special_lbl = gp.Label(app, '')
confirm_lbl = gp.Label(app, '')

def check_password_strength(event):
    password = password_input.text
    confirm_password = confirm_password_input.text
    score = 0

    # Check password length
    if len(password) < 8:
        len_lbl.text = '✖ 8 characters'
    else:
        len_lbl.text = '✔ 8 characters'
        score += 20

    # Check for numbers
    if any(char.isdigit() for char in password):
        num_lbl.text = '✔ Number (0-9)'
        score += 20
    else:
        num_lbl.text = '✖ Number (0-9)'

    # Check for lowercase characters
    if any(char.islower() for char in password):
        lowercase_lbl.text = '✔ Lowercase letters'
        score += 20
    else:
        lowercase_lbl.text = '✖ Lowercase letters'

    # Check for uppercase characters
    if any(char.isupper() for char in password):
        uppercase_lbl.text = '✔ Uppercase letters'
        score += 20
    else:
        uppercase_lbl.text = '✖ Uppercase letters'

    # Check for special characters
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    if any(char in special_chars for char in password):
        special_lbl.text = '✔ Special characters'
        score += 20
    else:
        special_lbl.text = '✖ Special characters'

    # Check password confirmation
    if password == confirm_password:
        confirm_lbl.text = '✔ Passwords match'
    else:
        confirm_lbl.text = '✖ Passwords do not match'

    # Display overall strength
    strength_text = f'Password Strength: {score}%'
    strength_lbl.text = strength_text

# Layout the components in the main window
app.set_grid(9, 2)
app.add(gp.Label(app, 'Enter password:'), 1, 1, align='right')
app.add(password_input, 1, 2)
app.add(gp.Label(app, 'Confirm password:'), 2, 1, align='right')
app.add(confirm_password_input, 2, 2)
app.add(len_lbl, 3, 2)
app.add(num_lbl, 4, 2)
app.add(lowercase_lbl, 5, 2)
app.add(uppercase_lbl, 6, 2)
app.add(special_lbl, 7, 2)
app.add(confirm_lbl, 8, 2)
strength_lbl = gp.Label(app, '')
app.add(strength_lbl, 9, 2)

# Bind the check_password_strength function to the password inputs
password_input.add_event_listener('change', check_password_strength)
confirm_password_input.add_event_listener('change', check_password_strength)

# Create a menu for Help and About
menu = gp.Menu(app)
menu.add_item('Help', help_window.show)
menu.add_item('About', about_window.show)
app.set_menu(menu)

# Run the application
app.run()
