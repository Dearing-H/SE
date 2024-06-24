import gooeypie as gp

# Create the main application window
app = gp.GooeyPieApp('BOSSBREAK')

# Create the second window (Help)
my_subwindow = gp.Window(app, 'Help')
my_subwindow.width = 400
my_subwindow.height = 300
my_subwindow.set_grid(3, 1)
help_text = gp.Label(my_subwindow, 'BOSSBREAK Designed and Developed by Harrison Dearing is a program that is designed to provide you with the strength level of your password. BOSSBREAK has been released using a GUI public license, currently equipped with the following features: Password Length: Longer passwords are stronger and more effective, choose between 10, 12, and 14; Password Complexity: Mix of characters.')
my_subwindow.add(help_text, 1, 1, align='center')

# Create the third window (About)
my_subwindow2 = gp.Window(app, 'About')
my_subwindow2.width = 400
my_subwindow2.height = 300
my_subwindow2.set_grid(3, 1)
about_text = gp.Label(my_subwindow2, 'Hello')
my_subwindow2.add(about_text, 1, 1, align='center')

# Set app properties
app.width = 600
app.height = 300
app.title = "BOSSBREAK"

checkbox_true = "✅"
checkbox_false = "❌"

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
        confirm_lbl.text = ''
    else:
        confirm_lbl.text = '✖ A password confirmation is required'

    # Check if password meets all criteria
    if score == 100 and password == confirm_password:
        confirm_lbl.text = '✔ Password meets all requirements'
    else:
        confirm_lbl.text = '✖ Password does not match the requirements'

def toggle_password_visibility(event):
    password_input.secret = not password_input.secret
    confirm_password_input.secret = not confirm_password_input.secret
    if password_input.secret:
        show_password_checkbox.text = 'Show password ' + checkbox_true
    else:
        show_password_checkbox.text = 'Hide password ' + checkbox_false

def open_help_window(event):
    my_subwindow.show()

def open_about_window(event):
    my_subwindow2.show()

# Create buttons and add event listeners
check_btn = gp.Button(app, 'Check Password Strength', check_password_strength)
show_password_checkbox = gp.Checkbox(app, 'Show password')
show_password_checkbox.add_event_listener('change', toggle_password_visibility)
help_btn = gp.Button(app, 'Help', open_help_window)
about_btn = gp.Button(app, 'About', open_about_window)

# Arrange components in the grid
app.set_grid(11, 2)
app.add(password_input, 1, 1, colspan=2)
app.add(show_password_checkbox, 3, 1, colspan=2)
app.add(check_btn, 4, 1, colspan=2)
app.add(len_lbl, 5, 1, colspan=2)
app.add(num_lbl, 6, 1, colspan=2)
app.add(lowercase_lbl, 7, 1, colspan=2)
app.add(uppercase_lbl, 8, 1, colspan=2)
app.add(special_lbl, 9, 1, colspan=2)
app.add(confirm_lbl, 10, 1, colspan=2)
app.add(help_btn, 11, 1, colspan=1)
app.add(about_btn, 11, 2, colspan=1)

app.run()
