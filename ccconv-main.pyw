#GPL-3.0-only

from tkinter import *
import pyclip

MainWindow = Tk()
MainWindow.geometry("500x560")
MainWindow.title("ccconv")

MainWindow.config()

OutputText = ""

# Creating Text Areas and Code Labels
TextAreaInput = Text(
        MainWindow,
        height = 22,
        width = 18,
        relief = SUNKEN,
        bd = 2
        )
TextAreaOutput = Text(
        MainWindow,
        height = 22,
        width = 18,
        relief = SUNKEN,
        bd = 2
        )

CodeLabel1 = Label(
        MainWindow,
        text = "Input Code:"
        )
CodeLabel2 = Label(
        MainWindow,
        text = "Output Code:"
        )

# Setting the Font for Code Labels
CodeLabel1.config(
        font = ("Calibri", 10)
        )
CodeLabel2.config(
        font = ("Calibri", 10)
        )

# Placing Code Labels and Text Areas
CodeLabel1.place(
        x = 20,
        y = 15
        )
CodeLabel2.place(
        x = 330,
        y = 15
        )

TextAreaInput.place(
        x = 20,
        y = 40
        )
TextAreaOutput.place(
        x = 330,
        y = 40
        )

# Addresses for each region, the "A" stands for "Addresses"
A_NTSCJ = list(["8107BDC0","8107BDC2","8107BDC4","8107BDC6","8107BDC8","8107BDCA","8107BDCC","8107BDCE","8107BDD8","8107BDDA","8107BDDC","8107BDDE","8107BDE0","8107BDE2","8107BDE4","8107BDE6","8107BDF0","8107BDF2","8107BDF4","8107BDF6","8107BDF8","8107BDFA","8107BDFC","8107BDFE","8107BE08","8107BE0A","8107BE0C","8107BE0E","8107BE10","8107BE12","8107BE14","8107BE16","8107BE20","8107BE22","8107BE24","8107BE26","8107BE28","8107BE2A","8107BE2C","8107BE2E","8107BE38","8107BE3A","8107BE3C","8107BE3E","8107BE40","8107BE42","8107BE44","8107BE46"])
A_NTSCU = list(["8107EC20","8107EC22","8107EC24","8107EC26","8107EC28","8107EC2A","8107EC2C","8107EC2E","8107EC38","8107EC3A","8107EC3C","8107EC3E","8107EC40","8107EC42","8107EC44","8107EC46","8107EC50","8107EC52","8107EC54","8107EC56","8107EC58","8107EC5A","8107EC5C","8107EC5E","8107EC68","8107EC6A","8107EC6C","8107EC6E","8107EC70","8107EC72","8107EC74","8107EC76","8107EC80","8107EC82","8107EC84","8107EC86","8107EC88","8107EC8A","8107EC8C","8107EC8E","8107EC98","8107EC9A","8107EC9C","8107EC9E","8107ECA0","8107ECA2","8107ECA4","8107ECA6"])
A_PAL = list(["810742E0","810742E2","810742E4","810742E6","810742E8","810742EA","810742EC","810742EE","810742F8","810742FA","810742FC","810742FE","81074300","81074302","81074304","81074306","81074310","81074312","81074314","81074316","81074318","8107431A","8107431C","8107431E","81074328","8107432A","8107432C","8107432E","81074330","81074332","81074334","81074336","81074340","81074342","81074344","81074346","81074348","8107434A","8107434C","8107434E","81074358","8107435A","8107435C","8107435E","81074360","81074362","81074364","81074366"])
A_SHINDOU = list(["8107BDC0","8107BDC2","8107BDC4","8107BDC6","8107BDC8","8107BDCA","8107BDCC","8107BDCE","8107BDD8","8107BDDA","8107BDDC","8107BDDE","8107BDE0","8107BDE2","8107BDE4","8107BDE6","8107BDF0","8107BDF2","8107BDF4","8107BDF6","8107BDF8","8107BDFA","8107BDFC","8107BDFE","8107BE08","8107BE0A","8107BE0C","8107BE0E","8107BE10","8107BE12","8107BE14","8107BE16","8107BE20","8107BE22","8107BE24","8107BE26","8107BE28","8107BE2A","8107BE2C","8107BE2E","8107BE38","8107BE3A","8107BE3C","8107BE3E","8107BE40","8107BE42","8107BE44","8107BE46"])

# Code Region Dropdown Menus
CodeRegionOptions = [
        "NTSC-J",
        "NTSC-U",
        "PAL",
        "Shindou"
]

DropInput = StringVar()
DropInput.set(CodeRegionOptions[1])
DropOutput = StringVar()
DropOutput.set(CodeRegionOptions[0])

DropI = OptionMenu(
        MainWindow,
        DropInput,
        *CodeRegionOptions
        )

DropO = OptionMenu(
        MainWindow,
        DropOutput,
        *CodeRegionOptions
        )

DropI.place(
        x = 20,
        y = 431
        )
DropO.place(
        x = 330,
        y = 431
        )

def RegionLabel(LabelName, x, y):
    LabelName = Label(
            MainWindow,
            text="Region:"
            )
    
    LabelName.config(
            font = ("Calibri", 10)
            )
    
    LabelName.place(
            x = x,
            y = y
            )

def Convert():
    InputText = str(TextAreaInput.get("1.0", END))

    if DropInput.get() == "NTSC-J":
        ChosenListInput = A_NTSCJ
    elif DropInput.get() == "NTSC-U":
        ChosenListInput = A_NTSCU
    elif DropInput.get() == "PAL":
        ChosenListInput = A_PAL
    else:
        ChosenListInput = A_SHINDOU
    
    if DropOutput.get() == "NTSC-J":
        ChosenListOutput = A_NTSCJ
    elif DropOutput.get() == "NTSC-U":
        ChosenListOutput = A_NTSCU
    elif DropOutput.get() == "PAL":
        ChosenListOutput = A_PAL
    else:
        ChosenListOutput = A_SHINDOU
    
    count = 0
    for item in ChosenListInput:
        InputText = InputText.replace(
                item,
                ChosenListOutput[count]
                )
        OutputText = InputText
        count += 1

    TextAreaOutput.delete(
            "1.0", END
            )
    TextAreaOutput.insert(
            "1.0", OutputText
            )

def ConvertButton(x, y):
    ConvertButton = Button(
            MainWindow,
            text="Convert",
            font = ("Calibri", 16),
            command = Convert
            )
    ConvertButton.place(
            x = x,
            y = y
            )

def Copy():
    pyclip.copy(
            TextAreaOutput.get(
            "1.0", END
            )
            )

def CopyButton(x, y):
    CopyButton = Button(
        MainWindow,
        text="Copy to clipboard",
        font = ("Calibri", 10),
        command = Copy
        )
    CopyButton.place(
            x = x,
            y = y
            )

def Paste():
    TextAreaInput.delete(
            "1.0", END
            )
    TextAreaInput.insert(
            "1.0", pyclip.paste(text = True)
            )

def PasteButton(x, y):
    PasteButton = Button(
        MainWindow,
        text="Paste from clipboard",
        font = ("Calibri", 10),
        command = Paste
        )
    PasteButton.place(
            x = x,
            y = y
            )

def AboutLabel(anchor):
    AboutLabel = Label(
            MainWindow,
            text = "ccconv v1.1.0\nMade by vdolya\nMy GitHub: https://github.com/vazhka-dolya"
            )

    AboutLabel.place(
            relx = 0.5,
            rely = 1.0,
            anchor = anchor
            )

RegionLabel("Label1", 20, 410)
RegionLabel("Label2", 330, 410)

ConvertButton(210, 190)

CopyButton(330, 470)
PasteButton(20, 470)

AboutLabel("s")

MainWindow.resizable(False, False)

MainWindow.mainloop()
