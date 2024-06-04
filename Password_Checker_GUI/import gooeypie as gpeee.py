import gooeypie as gp


# Create the GooeyPie app
app = gp.GooeyPieApp()

# Set app properties
app.width = 600
app.length = 600
app.title = "Password Checker"

# Define function to check password
def test(event):
    password = user_inp.get_text()
    errors = []

    # Check for uppercase letter
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")

    # Check for lowercase letter
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")

    # Check for special character
    if not any(char in str.punctuation for char in password):
        errors.append("Password must contain at least one special character.")

    # Check for at least two special characters
    if len([char for char in password if char in str.punctuation]) < 2:
        errors.append("Password must contain at least two special characters.")

    # Display errors or indicate strong password
    if errors:
        status_lbl.set_text("\n".join(errors))
    else:
        status_lbl.set_text("Password is strong.")

# Create GUI elements
user_lbl = gp.Label(app, "Password")
user_inp = gp.Input(app)
login_btn = gp.Button(app, 'Checker', test)
status_lbl = gp.Label(app, '')

# Set grid layout
app.set_grid(4, 1)
app.add(user_lbl, 1, 1)
app.add(user_inp, 1, 2)
app.add(login_btn, 3, 2)
app.add(status_lbl, 4, 2)

# Run the app
app.run()

