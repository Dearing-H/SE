import gooeypie as gp
import pyhibp
from pyhibp import pwnedpasswords as pw
import pyperclip

# Set the user agent for the HIBP API
pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")

# Create the main application window
app = gp.GooeyPieApp('BOSSBREAK')
app.width = 600
app.height = 400
app.title = "BOSSBREAK"
app.icon = 'lock.ico'  # Add a lock icon to the window

# Set the background color of the window
app.bg_color = '#f0f0f0'

# Create a logo label
logo_lbl = gp.Label(app, 'BOSSBREAK', font_size=24, font_bold=True)
logo_lbl.bg_color = '#333'
logo_lbl.text_color = '#fff'
app.add(logo_lbl, 1, 1, colspan=3)

# Create the password input field
password_input = gp.Secret(app, placeholder='Enter your password')
password_input.width = 300
app.add(password_input, 2, 1, colspan=2)

# Create a checkbox to toggle password visibility
show_password_checkbox = gp.Checkbox(app, 'Show password')
show_password_checkbox.width = 150
app.add(show_password_checkbox, 2, 2)

# Create a button to check password strength
check_btn = gp.Button(app, 'Check Password Strength', check_password_strength)
check_btn.width = 150
app.add(check_btn, 3, 1, colspan=2)

# Create labels to display password strength feedback
len_lbl = gp.Label(app, '', font_size=12)
case_lbl = gp.Label(app, '', font_size=12)
num_lbl = gp.Label(app, '', font_size=12)
special_lbl = gp.Label(app, '', font_size=12)
score_lbl = gp.Label(app, '', font_size=12)
breach_lbl = gp.Label(app, '', font_size=12)

app.add(len_lbl, 4, 1, colspan=2)
app.add(case_lbl, 5, 1, colspan=2)
app.add(num_lbl, 6, 1, colspan=2)
app.add(special_lbl, 7, 1, colspan=2)
app.add(score_lbl, 8, 1, colspan=2)
app.add(breach_lbl, 9, 1, colspan=2)

# Create a button to copy the password to the clipboard
copy_btn = gp.Button(app, 'Copy to Clipboard', copy_to_clipboard)
copy_btn.width = 150
app.add(copy_btn, 10, 1, colspan=2)

# Create a label to display the copy status
status_lbl = gp.Label(app, '', font_size=12)
app.add(status_lbl, 11, 1, colspan=2)

# Create a help window
my_subwindow = gp.Window(app, 'Help')
my_subwindow.width = 400
my_subwindow.height = 300
my_subwindow.set_grid(3, 1)
help_text = gp.Label(my_subwindow, 'BOSSBREAK designed and developed by Harrison Dearing is a program that is designed to provide you with a strength level of your password.'
                    'BOSSBREAK has been released using a GUI public license, currently equipped with the following features:'
                    'Password Length: Longer passwords are stronger and more effective, choose between 10, 12, and 14 '
                    'Password Complexity: Mix of ')
my_subwindow.add(help_text, 1, 1, align='center')

# Create an about window
my_subwindow2 = gp.Window(app, 'About')
my_subwindow2.width = 400
my_subwindow2.height = 300
my_subwindow2.set_grid(3, 1)
About_text = gp.Label(my_subwindow2, 'Hello')
my_subwindow2.add(About_text, 1, 1, align='center')

# Create buttons to open the help and about windows
check_btn2 = gp.Button(app, 'Help', open_help_window)
check_btn3 = gp.Button(app, 'About', open_about_window)

app.add(check_btn2, 10, 2, colspan=2)
app.add(check_btn3, 10, 3, colspan=2)

# Lock the window size
app.resizable = False

app.run()