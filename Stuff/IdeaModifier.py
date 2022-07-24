import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import ImageTk, Image
from os.path import exists
from os import getcwd

questionMarkImage = getcwd() + "/Stuff/QuestionMark.png"
imageDimension = 35

class IdeaModifier:
    def __init__(self, parentPanel, fileConfig):
        self.fileConfig = fileConfig
        self.fileConfig.listeners.append(self)
        self.modifiers = fileConfig.readModifiers()
        self.modifierPanel = tk.PanedWindow(parentPanel, orient=tk.VERTICAL)
        self.modifierPanel.pack(side=tk.TOP)
        image = Image.open(questionMarkImage).resize((imageDimension, imageDimension), Image.ANTIALIAS)
        photoImage = ImageTk.PhotoImage(image)
        self.modifierImage = tk.Label(self.modifierPanel, image=photoImage)
        self.modifierImage.image = photoImage
        self.modifierImage.pack(side=tk.LEFT)
        self.stringVar = tk.StringVar()
        self.stringVar.trace('w', self.onComboboxChange)
        self.modifierField = AutocompleteCombobox(self.modifierPanel, width=32, completevalues=list(self.modifiers.keys()), textvar=self.stringVar)
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

    def updateModifierIcon(self):
        comboBoxText = self.modifierField.get()
        imageFileName = questionMarkImage
        supposedIconFileName = "{}/{}.dds".format(self.fileConfig.modifierIconDirectory, comboBoxText)
        if exists(supposedIconFileName):
            imageFileName = supposedIconFileName
        image = Image.open(imageFileName).resize((imageDimension, imageDimension), Image.ANTIALIAS)
        photoImage = ImageTk.PhotoImage(image)
        self.modifierImage.configure(image=photoImage)
        self.modifierImage.image = photoImage

    def onComboboxChange(self, index, value, op):
        comboBoxText = self.modifierField.get()
        if comboBoxText in self.modifiers:
            self.modifierAmount.delete(0, tk.END)
            self.modifierAmount.insert(0, self.modifiers[comboBoxText].baseValue)
            # TODO: change the default vaue if blank
        self.updateModifierIcon()