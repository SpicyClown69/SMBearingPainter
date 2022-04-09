from tkinter.filedialog import askopenfilename
hexmap = ["222222", "323000", "375000", "064023", "0a4444", "0a1d5a", "35086c", "520653", "472800"]
colourmap = ["Black", "Dark Yellow", "Dark Lime", "Dark Green", "Dark Turquoise", "Dark Blue", "Dark Purple", "Dark Pink", "Dark Red", "Brown"]
Colour = ""
file = askopenfilename()
def askColour():
    global Colour
    Colour = input("Choose a color from:\n" + str(colourmap).replace("[","").replace("]","") + " (Case Sensitive)\n")
    if Colour in colourmap:
        return
    else:
        print("Invalid Colour, try again:")
        askColour()
askColour()
index = 0
for i in colourmap:
    if i == Colour:
        hexcode = hexmap[index]
        print(hexcode)
    else:
        index += 1
filecontents = ""
with open(file, "r") as f:
    filecontents = f.read()
with open(file, "w") as f:
    f.write(filecontents.replace(hexcode, "bb6033ff"))
