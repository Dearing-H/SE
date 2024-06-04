import gooeypie as gp

def on_text_change(event):
    text = text_box.text
    print(text)

    if text == "Fongy":
        label.text = "I miss my hair line"
    else:
        check_length(event)  # Call the length checking function when text changes

def check_length(event):
    input_text = text_box.text  # Get the text from the text box
    length = len(input_text)  # Get the length of the text
    
    if length <= 10:
        label.text = f'Text length is {length}. It is within the limit.'
    else:
        label.text = f'Text length is {length}. It exceeds the limit of 10 characters.'

app = gp.GooeyPieApp('The giver')

text_box = gp.Textbox(app)
text_box.add_event_listener('change', on_text_change)

label = gp.Label(app, "")

app.set_grid(2,1)
app.add(text_box,1, 1)
app.add(label, 2, 1)

app.run()
