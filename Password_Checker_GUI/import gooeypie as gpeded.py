import gooeypie as gp

app = gp.GooeyPieApp('BOSSBREAK')

# Set app properties
app.width = 600
app.height = 400
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
        score -= 10
    elif len(password) > 16:
        len_lbl.text = 'Password is too long, maximum 16 characters'
        score -= 5
    else:
        len_lbl.text = 'Password length is good'
        score += 20

    # Check for uppercase and lowercase characters
    if password.islower():
        case_lbl.text = 'Password is all lowercase, add uppercase letters'
        score -= 5
    elif password.isupper():
        case_lbl.text = 'Password is all uppercase, add lowercase letters'
        score -= 5
    else:
        case_lbl.text = 'Password has mixed case characters'
        score += 20

    # Check for numbers
    if any(char.isdigit() for char in password):
        num_lbl.text = 'Password contains numbers'
        score += 20
    else:
        num_lbl.text = 'Password should contain at least one number'
        score -= 5

    # Check for special characters
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    if any(char in special_chars for char in password):
        special_lbl.text = 'Password contains special characters'
        score += 20
    else:
        special_lbl.text = 'Password should contain at least one special character'
        score -= 5

    # Check for repeated characters
    if len(password) != len(set(password)):
        score -= 10
    
    # Calculate and display the score
    score_lbl.text = f'Your password score is {score}'

def toggle_password_visibility(event):
    password_input.secret = not password_input.secret
    if password_input.secret:
        show_password_checkbox.text = 'Show password' + checkbox_true
    else:
        show_password_checkbox.text = 'Hide password' + checkbox_false

# Create buttons and checkboxes
check_btn = gp.Button(app, 'Check Password Strength', check_password_strength)
show_password_checkbox = gp.Checkbox(app, 'Show password')
show_password_checkbox.add_event_listener('change', toggle_password_visibility)

# Arrange components in the grid
app.set_grid(8, 2)
app.add(password_input, 1, 1, colspan=2)
app.add(show_password_checkbox, 2, 1, colspan=2)
app.add(check_btn, 3, 1, colspan=2)
app.add(len_lbl, 4, 1, colspan=2)
app.add(case_lbl, 5, 1, colspan=2)
app.add(num_lbl, 6, 1, colspan=2)
app.add(special_lbl, 7, 1, colspan=2)
app.add(score_lbl, 8, 1, colspan=2)

app.run()
