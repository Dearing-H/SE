import gooeypie as gp

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
def check_password(event):
    password = password_input.text
    special_characters = "!@#$%^&*()-_+=<>?{}[]|\\/.:,;\"'`~"
    errors = []
    
    # Clear previous error labels
    for label in error_labels:
        label.text = ""

    # Check for length
    if len(password) <= 16:
        errors.append("Password must be longer than 16 characters.")
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter.")
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter.")
    
    # Check for at least one special character
    if not any(char in special_characters for char in password):
        errors.append("Password must contain at least one special character.")
    
    # Check for at least two special characters
    if sum(1 for char in password if char in special_characters) < 2:
        errors.append("Password must contain at least two special characters.")

    # Display errors or success message
    if errors:
        for i, error in enumerate(errors):
            error_labels[i].text = checkbox_false + " " + error
        success_label.text = ""
        progress_bar.value = (5 - len(errors)) * 20
    else:
        success_label.text = checkbox_true + " Password is strong."
        for label in error_labels:
            label.text = ""
        progress_bar.value = 100

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

success_label = gp.Label(app, '')
error_labels = [gp.Label(app, '') for _ in range(5)]  # Assuming max 5 errors

progress_bar = gp.Progressbar(app, 0, 100)
progress_bar.value = 0

# Set grid layout and add elements to the app
app.set_grid(12, 1)
app.add(password_label, 1, 1, align='center')
app.add(password_input, 2, 1, align='center')
app.add(show_password_checkbox, 3, 1, align='center')
app.add(check_button, 4, 1, align='center')
app.add(progress_bar, 5, 1, align='center')
app.add(success_label, 6, 1, align='center')

for i, label in enumerate(error_labels):
    app.add(label, 7 + i, 1, align='center')

# Run the app
app.run()
