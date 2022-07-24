from Stuff.FileConfig import FileConfig
from Stuff.Modifier import Modifier
from Stuff.IdeaModifier import IdeaModifier
import tkinter as tk
from os.path import exists

class IdeaSetGenerator:
    def __init__(self):
        self.ideas = [[], [], [], [], [], [], [], [], []]
        self.modifiers = dict()
        self.fileConfig = FileConfig()
        self.fileConfig.readModifiers()

        self.window = tk.Tk()
        self.window.geometry("400x825")
        self.window.title("Idea Set Geneator")

        menubar = tk.Menu(self.window)
        fileMenu = tk.Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Save", command=self.fileConfig.save())
        fileMenu.add_separator()
        fileMenu.add_command(label="Set Destination File")
        fileMenu.add_command(label="Load Modifiers", command=self.fileConfig.loadNewModifiersFile)
        fileMenu.add_command(label="Load Modifier Icons", command =self.fileConfig.loadNewModifierIconsDirectory)
        menubar.add_cascade(label="File", menu=fileMenu)
        self.window.config(menu=menubar)

        tagPanel = self.createTagPanel()
        traditions = self.createIdeaSection("Tradition(s):", ideaNum=0, startingIdeas=2)
        idea1 = self.createIdeaSection("Idea One:", ideaNum=1, startingIdeas=1)
        idea2 = self.createIdeaSection("Idea Two:", ideaNum=2, startingIdeas=1)
        idea3 = self.createIdeaSection("Idea Three:", ideaNum=3, startingIdeas=1)
        idea4 = self.createIdeaSection("Idea Four:", ideaNum=4, startingIdeas=1)
        idea5 = self.createIdeaSection("Idea Five:", ideaNum=5, startingIdeas=1)
        idea6 = self.createIdeaSection("Idea Six:", ideaNum=6, startingIdeas=1)
        idea7 = self.createIdeaSection("Idea Seven:", ideaNum=7, startingIdeas=1)
        ambition = self.createIdeaSection("Ambition(s):", ideaNum=8, startingIdeas=1)

    def startMainLoop(self):
        self.window.mainloop()

    def createTagPanel(self):
        panel = tk.PanedWindow(self.window, orient=tk.VERTICAL)
        panel.pack(side=tk.TOP)
        tagLabel = tk.Label(panel, text="Tag:")
        tagLabel.pack(side=tk.LEFT)
        tagEntry = tk.Entry(panel, width=5, justify="center")
        tagEntry.pack(side=tk.LEFT)
        randomIdeasButton = tk.Button(panel, text="?")
        randomIdeasButton.pack(side=tk.LEFT)
        return panel

    def createIdeaSection(self, title, ideaNum, startingIdeas):
        panel = tk.PanedWindow(self.window, orient=tk.VERTICAL)
        panel.pack(side=tk.TOP)
        modifiersPanel = tk.PanedWindow(self.window, orient=tk.VERTICAL)
        modifiersPanel.pack(side=tk.TOP)
        ideaLabel = tk.Label(panel, text=title)
        ideaLabel.pack(side=tk.LEFT)
        createNewIdeaModifierLambda = (lambda : self.ideas[ideaNum].append(IdeaModifier(modifiersPanel, self.fileConfig)))
        addIdeaButton = tk.Button(panel, text="+", command=createNewIdeaModifierLambda)
        addIdeaButton.pack(side=tk.LEFT)
        removeIdeaButton = tk.Button(panel, text="-", command=(lambda : self.removeModifier(ideaNum)))
        removeIdeaButton.pack(side=tk.LEFT)
        for i in range(0, startingIdeas):
            self.ideas[ideaNum].append(IdeaModifier(modifiersPanel, self.fileConfig))

    def loadModifiers(self, filePath):
        if exists(filePath):
            f = open(filePath, 'r')
            for line in f:
                name, baseValue, description, effectType, versionAdded = line.split(";")
                self.modifiers[name] = Modifier(name, baseValue, description, effectType, versionAdded)
            f.close()
            for idea in self.ideas:
                for ideaModifier in idea:
                    ideaModifier.updateModifiers(self.modifiers)
        else:
            tk.messagebox.showinfo("File Not Found", "Could not find the following file for the modifiers: {}".format(filePath))

    def removeModifier(self, ideaNum):
        if len(self.ideas[ideaNum]) > 0:
            modifier = self.ideas[ideaNum].pop()
            modifier.destroy()

def populateIdeaSetText():
    ideaSetText = """{} = {{\n
                \tstart = {{\n
                \t\t{}\n
                \t}}\n\n
                \tbonus = {{
                \t\t{}\n
                \t}}\n\n
                \ttrigger = {{
                \t\ttag = {}\n
                \t}}\n\n"""

def changeModifierImageLocation(directory):
    if exists(directory):
        for idea in ideas:
            for ideaModifier in idea:
                ideaModifier.modifierIconDirectory = directory
    else:
        tk.messagebox.showinfo("File Not Found", "Could not find the following directory for the modifier icons: {}".format(directory))

if __name__ == "__main__":
    ideaSetGenerator = IdeaSetGenerator()
    ideaSetGenerator.startMainLoop()