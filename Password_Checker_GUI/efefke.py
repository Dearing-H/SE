import gooeypie as gp
global pass_inp
global len_lbl
global case_lbl
global score

# Create the GooeyPie app
app = gp.GooeyPieApp('BOSSBREAK')

# Set app properties
app.width = 600
app.height = 600
app.title = "BOSSBREAK"



checkbox_true = "✅"
checkbox_false = "❌"


# step 1 
# go through each function and get it to print to the console as a test
# work on grid and put in all the widgets
# then link back the check button to "check password" to all of the functions from above
    

def check_len_8(password, errors):
    if len(password_input.text) <= 16:
        print("Password is too short, longer than 16 characters please")
        # len_lbl.text = 'Password is too short, longer than 16 characters please'
        # errors.append(len_lbl.text)
    else:
        print('Password is long enough, good job!')

        # len_lbl.text = 'Password is long enough, good job!'


def check_len_16(password):
    if len(password_input.text) <= 16:
        print("Password is too short, longer than 16 characters please")
        len_lbl.text = 'Password is too short, longer than 16 characters please'
    else:
        len_lbl.text = 'Password is long enough, good job!'

def check_lcase(password):
    if pass_inp.text.islower():
        case_lbl.text = 'Password is all uppercase, please add lowercase letters'
    else:
        case_lbl.text = 'Password has lowercase characters'


def check_Ucase(pasword):
    if pass_inp.text.isupper():
        case_lbl.text = 'Password is all lowercase, please add uppercase letters'
    else:
        case_lbl.text = 'Password has uppercase characters'


def check_symbol(password):
    symbols = "!@#$%^&*()-_+=<>?{}[]|\\/.:,;\"'`~"
    for letter in password:
        if letter in symbols:
            return True
        
    return False


# Function to check the password strength
def check_password(event):
    password = password_input.text
    errors = []
    check_len_8(password, errors)




    

#     # Check for at least one uppercase letter
#     if not any(char.isupper() for char in password):
#         errors.append(f" {checkbox_false} Password must contain at least one uppercase letter.")
    
#     # Check for at least one lowercase letter
#     if not any(char.islower() for char in password):
#         errors.append("Password must contain at least one lowercase letter.")
    
#     # Check for at least one special character
#     if not any(char in special_characters for char in password):
#         errors.append("Password must contain at least one special character.")
    
#     # Check for at least two special characters
#     if sum(1 for char in password if char in special_characters) < 2:
#         errors.append("Password must contain at least two special characters.")

#     # Display errors or success message
#     if errors:
#         status_label.text = "\n".join(errors)
#     else:
#         status_label.text = "Password is strong."

# Function to toggle the visibility of the password


def toggle_password_visibility(event):
    password_input.toggle()

# Create GUI elements
password_label = gp.Label(app, "Password")
password_input = gp.Secret(app)
password_input.width = 50

show_password_checkbox = gp.Checkbox(app, 'Show password')
show_password_checkbox.add_event_listener('change', toggle_password_visibility)

check_button = gp.Button(app, 'Check', check_password)
status_label = gp.Label(app, '')

# Set grid layout
app.set_grid(5, 1)
app.add(password_label, 1, 1)
app.add(password_input, 2, 1)
app.add(show_password_checkbox, 3, 1)
app.add(check_button, 4, 1)
app.add(status_label, 5, 1)

# Run the app
app.run()



