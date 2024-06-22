import gooeypie as gp

def check_length(password):
    return len(password) >= 8

def check_numbers(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def check_special_chars(password):
    special_chars = "!@#$%^&*()_+[]{}|;:,.<>?~"
    for char in password:
        if char in special_chars:
            return True
    return False

def update_strength(event):
    password = password_input.get()
    strength = ""

    if check_length(password):
        strength += "Length: ✅\n"
    else:
        strength += "Length: ❌\n"

    if check_numbers(password):
        strength += "Numbers: ✅\n"
    else:
        strength += "Numbers: ❌\n"

    if check_special_chars(password):
        strength += "Special Characters: ✅\n"
    else:
        strength += "Special Characters: ❌\n"

    strength_label.set_text(strength)

def toggle_password_visibility(event):
    if password_input.secret:
        password_input.secret = False
        toggle_button.text = 'Hide Password'
    else:
        password_input.secret = True
        toggle_button.text = 'Show Password'

def main():
    global password_input, strength_label, toggle_button
    
    # Create the app
    app = gp.GooeyPieApp('BOSSBREAK')

    # Set app properties
    app.width = 600
    app.height = 600
    app.title = "BOSSBREAK"
    app.bg_color = "#f0f0f0"

    # Set up the grid
    app.set_grid(5, 1)

    # Create input and label
    password_input = gp.Input(app, secret=True)
    strength_label = gp.Label(app, "")
    check_button = gp.Button(app, "Check Password", update_strength)
    toggle_button = gp.Button(app, "Show Password", toggle_password_visibility)

    # Add input, buttons, and label to the app
    app.add(password_input, 1, 1)
    app.add(check_button, 2, 1)
    app.add(toggle_button, 3, 1)
    app.add(strength_label, 4, 1)

    # Run the app
    app.run()

if __name__ == '__main__':
    main()
