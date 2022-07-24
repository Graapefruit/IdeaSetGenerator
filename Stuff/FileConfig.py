from os import getcwd
from os.path import exists
from Stuff.Modifier import Modifier
from tkinter import filedialog as fd

SETTINGS_FILE = "Settings.txt"

class FileConfig:
    def __init__(self):
        self.listeners = []
        self.modifierFile = ""
        self.questionMarkIcon = ""
        self.modifierIconDirectory = ""
        if exists(SETTINGS_FILE):
            for line in open(SETTINGS_FILE, 'r'):
                lineSplit = line.split('=')
                if len(lineSplit) > 1:
                    fileKey =  lineSplit[0].strip()
                    fileValue = lineSplit[1].strip()
                    if fileKey == "modifiers":
                        self.modifierFile = fileValue
                    elif fileKey == "questionMark":
                        self.questionMarkIcon = fileValue
                    elif fileKey == "modifierIcons":
                        self.modifierIconDirectory = fileValue
        else:
            self.updateSettingsFile()
            print("{} could not be found. One has been made and your file settings will be saved to here".format(SETTINGS_FILE))

    def updateSettingsFile(self):
        f = open(SETTINGS_FILE, 'w')
        f.write("modifiers = " + self.modifierFile)
        f.write("\nquestionMark = " + self.questionMarkIcon)
        f.write("\nmodifierIcons = " + self.modifierIconDirectory)
        f.close()

    def loadNewModifiersFile(self):
        openedFolder = fd.askopenfilename()
        if exists(openedFolder):
            self.modifierFile = openedFolder
            modifiers = self.readModifiers()
            for listener in self.listeners:
                listener.updateModifiers(modifiers)
            self.updateSettingsFile()
        else:
            print("Could not find the following file for the modifiers: {}".format(self.modifierFile))

    def loadNewModifierIconsDirectory(self):
        openedFile = fd.askdirectory()
        if exists(openedFile):
            self.modifierIconDirectory = openedFile
            self.updateSettingsFile()
            for listener in self.listeners:
                listener.updateModifierIcon()
        else:
            print("Could not find the following file for the modifiers: {}".format(self.modifierFile))

    def readModifiers(self):
        modifiers = dict()
        if exists(self.modifierFile):
            f = open(self.modifierFile, 'r')
            for line in f:
                name, baseValue, description, effectType, versionAdded = line.split(";")
                modifiers[name] = Modifier(name, baseValue, description, effectType, versionAdded)
            f.close()
        return modifiers