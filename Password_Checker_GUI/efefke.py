import gooeypie as gp
global pass_inp
global len_lbl


# Create the GooeyPie app
app = gp.GooeyPieApp('BOSSBREAK')

# Set app properties
app.width = 600
app.height = 600
app.title = "BOSSBREAK"


# Useful emoji
checkbox_true = "✅"
checkbox_false = "❌"


# Function to check the password strength
def check_password():
    password = password_input.text
    errors = []

    # Define special characters
    special_characters = "!@#$%^&*()-_+=<>?{}[]|\\/.:,;\"'`~"

def check_len():
    if len(pass_inp.text) <= 16:
        len_lbl.text = 'Password is too short, longer than 16 characters please'
    else:
        len_lbl.text = 'Password is long enough, good job!'

# def check_lcase():
#     if pass_inp.text.islower():
#         case_lbl.text = 'Password is all uppercase, please add lowercase letters'
#     else:
#         case_lbl.text = 'Password has a good number of lowercase characters'

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
