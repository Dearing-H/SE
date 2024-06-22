import gooeypie as gp

app = gp.GooeyPieApp('BOSSBREAK')

# Set app properties
app.width = 600
app.height = 400
app.title = "BOSSBREAK"
score = 100

checkbox_true = "✅"
checkbox_false = "❌"


# Create UI components
password_input = gp.Input(app)
len_lbl = gp.Label(app, '')
case_lbl = gp.Label(app, '')
num_lbl = gp.Label(app, '')
special_lbl = gp.Label(app, '')
score_lbl = gp.Label(app, '')

def check_password_strength(event):
    global score
    password = password_input.text

    # Check password length
    if len(password) <= 12:
        len_lbl.text = 'Password is too short, longer than 12 characters please'
    elif len(password) <= 14:
        len_lbl.text = 'Password is too short, longer than 16 characters please'
    elif len(password) <= 16:
        len_lbl.text = 'Password is a good length, if need be you can use less characters'
    else:
        len_lbl.text = 'Password is too long, please use an option provided!'

    # Check for uppercase and lowercase characters
    if password.islower():
        case_lbl.text = 'Password is all lowercase, please add uppercase letters'
    elif password.isupper():
        case_lbl.text = 'Password is all uppercase, please add lowercase letters'
    else:
        case_lbl.text = 'Password has mixed case characters'



    
   # Check for numbers
    contains_number = False
    for char in password:
        if char.isdigit():
            contains_number = True

    if contains_number:
        num_lbl.text = 'Password contains numbers'
        
    else:
        num_lbl.text = 'Password should contain at least one number'

    # Check for special characters
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    contains_special = False
    for char in password:
        if char in special_chars:
            contains_special = True

    if contains_special:
        special_lbl.text = 'Password contains special characters'
    else:
        special_lbl.text = 'Password should contain at least one special character'

    score = 100
    if contains_number == True:
        score += 10
    
    score_lbl.text = f'Your password has a score of {score}'



def toggle_password_visibility(event):
    password_input.toggle()


check_btn = gp.Button(app, 'Check Password Strength', check_password_strength)
show_password_checkbox = gp.Checkbox(app, 'Show password')
show_password_checkbox.add_event_listener('change', toggle_password_visibility)




app.set_grid(8,2)
app.add(password_input, 1, 1, colspan=2)
app.add(show_password_checkbox, 2, 2)
app.add(check_btn, 3, 1, colspan=2)
app.add(len_lbl, 4, 1, colspan=2)
app.add(case_lbl, 5, 1, colspan=2)
app.add(num_lbl, 6, 1, colspan=2)
app.add(special_lbl, 7, 1, colspan=2)
app.add(score_lbl, 8, 1, colspan=2)

app.run()
