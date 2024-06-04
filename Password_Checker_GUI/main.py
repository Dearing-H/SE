import gooeypie as gp
#imports all of the classes downloaded via the pip install

app = gp.GooeyPieApp('Hello!')
#instanitae a "gooeypie"

app.width = 600
app.length = 400
app.title = "Password checker"

#setup grid
app.set_grid(2,1)

def sumbit(event):
    print("I work")


#create widgets
btn = gp.Button(app,"Submit", sumbit)
lbl = gp.Label(app, "This is a label")
#put stuff in grid
app.add(btn,1,1)
app.add(lbl,2,1)

app.run()