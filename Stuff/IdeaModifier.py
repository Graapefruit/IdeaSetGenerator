import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import ImageTk, Image
from os.path import exists

questionMarkImage = "/home/graham/Documents/EU4Stuff/IdeaSetGenerator/Stuff/QuestionMark.png"
imageDimension = 35

class IdeaModifier:
    def __init__(self, parentPanel, modifiers):
        self.modifiers = modifiers
        self.modifierPanel = tk.PanedWindow(parentPanel, orient=tk.VERTICAL)
        self.modifierPanel.pack(side=tk.TOP)
        image = Image.open(questionMarkImage).resize((imageDimension, imageDimension), Image.ANTIALIAS)
        photoImage = ImageTk.PhotoImage(image)
        self.modifierImage = tk.Label(self.modifierPanel, image=photoImage)
        self.modifierImage.image = photoImage
        self.modifierImage.pack(side=tk.LEFT)
        self.stringVar = tk.StringVar()
        self.stringVar.trace('w', self.onComboboxChange)
        self.modifierField = AutocompleteCombobox(self.modifierPanel, width=24, completevalues=list(modifiers.keys()), textvar=self.stringVar)
        self.modifierField.pack(side=tk.LEFT)
        self.modifierAmount = tk.Entry(self.modifierPanel, width=5)
        self.modifierAmount.pack(side=tk.LEFT)

    def destroy(self):
        self.modifierPanel.destroy()
        self.modifierField.destroy()
        self.modifierAmount.destroy()

    def updateModifiers(self, modifiers):
        self.modifierField["values"] = list(modifiers.keys())
        self.modifiers = modifiers

    def onComboboxChange(self, index, value, op):
        imageFileName = "/home/graham/Documents/EU4Stuff/IdeaSetGenerator/Stuff/QuestionMark.png"
        comboBoxText = self.modifierField.get()
        if comboBoxText in self.modifiers:
            self.modifierAmount.delete(0, tk.END)
            self.modifierAmount.insert(0, self.modifiers[comboBoxText].baseValue)
            # TODO: change the default vaue if blank
            # TODO: Variable icon location 
            iconFileName = "/home/graham/.steam/steam/steamapps/common/Europa Universalis IV/gfx/interface/ideas_EU4/{}.dds".format(comboBoxText)
            if exists(iconFileName):
                imageFileName = iconFileName
        image = Image.open(imageFileName).resize((imageDimension, imageDimension), Image.ANTIALIAS)
        photoImage = ImageTk.PhotoImage(image)
        self.modifierImage.configure(image=photoImage)
        self.modifierImage.image = photoImage
