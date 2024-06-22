import gooeypie as gp



# Create the main application window
app = gp.GooeyPieApp('BOSSBREAK')

# Create the second window
my_subwindow = gp.Window(app, 'Help')
my_subwindow.width = 400
my_subwindow.height = 300

my_subwindow.set_grid(3, 1)

help_text = gp.Label(my_subwindow, 'BOSSBREAk is a programm that is desgined to provide you with a strength level of your password')
my_subwindow.add(help_text, 1, 1, align='center')

my_subwindow2 = gp.Window(app, 'About')
my_subwindow2
my_subwindow2.width = 400
my_subwindow2.height = 300

my_subwindow2.set_grid(3, 1)

About_text = gp.Label(my_subwindow2, 'Hello')
my_subwindow2.add(About_text, 1, 1, align='center')



# Set app properties
app.width = 600
app.height = 300
app.title = "BOSSBREAK"

checkbox_true = "✅"
checkbox_false = "❌"

# Create UI components
password_input = gp.Secret(app)
len_lbl = gp.Label(app, '')
case_lbl = gp.Label(app, '')
num_lbl = gp.Label(app, '')
special_lbl = gp.Label(app, '')
score_lbl = gp.Label(app, '')

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

def toggle_password_visibility(event):
    password_input.secret = not password_input.secret
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

check_btn2 = gp.Button(app, 'Help', open_help_window)
check_btn3 = gp.Button(app, 'About', open_about_window)


# Arrange components in the grid
app.set_grid(11, 2)
app.add(password_input, 1, 1, colspan=2)
app.add(show_password_checkbox, 2, 1, colspan=2)
app.add(check_btn, 3, 1, colspan=2)
app.add(len_lbl, 4, 1, colspan=2)
app.add(case_lbl, 5, 1, colspan=2)
app.add(num_lbl, 6, 1, colspan=2)
app.add(special_lbl, 7, 1, colspan=2)
app.add(score_lbl, 8, 1, colspan=2)
app.add(check_btn2, 10, 1, colspan=2)
app.add(check_btn3, 10, 2, colspan=2)

app.run()
