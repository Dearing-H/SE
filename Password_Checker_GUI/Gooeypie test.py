import gooeypie as gp

def check_password_strength(password):
    strength = "Strong"
    uppercase_count = sum(1 for c in password if c.isupper())
    lowercase_count = sum(1 for c in password if c.islower())
    number_count = sum(1 for c in password if c.isdigit())
    symbol_count = sum(1 for c in password if not c.isalnum())

    if len(password) < 8:
        strength = "Weak"
    elif uppercase_count + lowercase_count + number_count + symbol_count < 3:
        strength = "Medium"

    return strength

def check_password(event):
    password = password_entry.text
    strength = check_password_strength(password)
    result_label.text = f"Password strength: {strength}"

app = gp.GooeyPieApp("Password Strength Checker")
app.width = 300

password_label = gp.Label(app, "Enter your password:")
password_entry = gp.Entry(app, width=20)  # Changed from Label to Entry
check_button = gp.Button(app, "Check", check_password)
result_label = gp.Label(app, "")

app.set_grid(4, 1)
app.add(password_label, 1, 1, align='center')
app.add(password_entry, 2, 1, align='center')
app.add(check_button, 3, 1, align='center')
app.add(result_label, 4, 1, align='center')

app.run()
