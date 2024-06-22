import gooeypie as gp

app = gp.GooeyPieApp('BOSSBREAK')

# Set app properties
app.width = 600
app.height = 600
app.title = "BOSSBREAK"
app.bg_color = "#f0f0f0"

checkbox_true = "✅"
checkbox_false = "❌"

# Create UI components
password_input = gp.Input(app)
len_lbl = gp.Label(app, '')
case_lbl = gp.Label(app, '')
check_btn = gp.Button(app, 'Check Password Strength', check_password_strength)

def check_password_strength(event):
    password = password_input.text

    def check_len_12(password):
        if len(password) <= 12:
            len_lbl.text = 'Password is too short, longer than 12 characters please'
        else:
            len_lbl.text = 'Password is long, can Choose between 14,16'


    def check_len_14(password):
        if len(password) <= 14:
            len_lbl.text = 'Password is too short, longer than 16 characters please'
        else:
            len_lbl.text = 'Password is long enough, good job!'

    def check_len_16(password):
        if len(password) <= 16:
            len_lbl.text = 'Password is a good length, if need be you can use less characters'
        else:
            len_lbl.text = 'Password is to Long please use an option provided!'


    def check_lcase(password):
        if password.islower():
            case_lbl.text = 'Password is all lowercase, please add uppercase letters'
        else:
            case_lbl.text = 'Password has uppercase characters'

    check_len_16(password)
    check_lcase(password)

# Add components to the app

