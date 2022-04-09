import tkinter as tk
from tkinter.filedialog import askopenfilename
window = tk.Tk()
window.config(bg="black")
window.geometry("200x100")
window.title("Bearing Painter")
label1 = tk.Label(text="Enter Color Code:", bg="black", fg="white")
label1.pack()
colorcodeui = tk.Entry(bg="white", fg="black")
colorcodeui.pack()
file = ""
def selectFile():
    global file
    file = askopenfilename()
def Start():
    global file
    bearingid = "4a1b886b-913e-4aad-b5b6-6e41b0db23a6"
    colorcode = str(colorcodeui.get())
    filesplit = []
    final = []
    with open(file, "r")as f:
        text = f.read()
        filesplit = text.split("\"color\":\"")
    for i in filesplit:
        if bearingid in i:
            final.append("\"color\":\"" + colorcode  + "\"" + i[7:])
        else:
            final.append("\"color\":\"" + i)
    with open(file, "w") as f:
        f.write("".join(final)[9:])
selectfile = tk.Button(text="Select File", bg="white", fg="black", command=selectFile)
selectfile.pack()
startbutton = tk.Button(text="Start", bg="white", fg="black",command=Start)
startbutton.pack()
window.mainloop()
