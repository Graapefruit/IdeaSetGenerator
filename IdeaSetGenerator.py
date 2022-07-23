from Stuff.Modifier import Modifier
from Stuff.IdeaModifier import IdeaModifier
import tkinter as tk
from tkinter import filedialog as fd
from os.path import exists

modifiers = []
modifierNameToData = dict()
ideas = [[], [], [], [], [], [], [], [], []]

def loadModifiers(filePath):
    if exists(filePath):
        f = open(filePath, 'r')
        for line in f:
            name, baseValue, description, effectType, versionAdded = line.split(";")
            modifiers.append(name)
            modifierNameToData[name] = Modifier(name, baseValue, description, effectType, versionAdded)
        for idea in ideas:
            for ideaModifier in idea:
                ideaModifier.modifierField["values"]=modifiers
    else:
        tk.messagebox.showinfo("File Not Found", "The following file does not exist: {}".format(filePath))

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

def createTagPanel(window):
    panel = tk.PanedWindow(window, orient=tk.VERTICAL)
    panel.pack(side=tk.TOP)
    tagLabel = tk.Label(panel, text="Tag:")
    tagLabel.pack(side=tk.LEFT)
    tagEntry = tk.Entry(panel, width=5, justify="center")
    tagEntry.pack(side=tk.LEFT)
    randomIdeasButton = tk.Button(panel, text="?")
    randomIdeasButton.pack(side=tk.LEFT)
    return panel

def createIdeaSection(window, title, ideaNum):
    panel = tk.PanedWindow(window, orient=tk.VERTICAL)
    panel.pack(side=tk.TOP)
    modifiersPanel = tk.PanedWindow(window, orient=tk.VERTICAL)
    modifiersPanel.pack(side=tk.TOP)
    ideaLabel = tk.Label(panel, text=title)
    ideaLabel.pack(side=tk.LEFT)
    createNewIdeaModifierLambda = (lambda : ideas[ideaNum].append(IdeaModifier(modifiersPanel, modifiers)))
    addIdeaButton = tk.Button(panel, text="+", command=createNewIdeaModifierLambda)
    addIdeaButton.pack(side=tk.LEFT)
    removeIdeaButton = tk.Button(panel, text="-", command=(lambda : removeModifier(ideaNum)))
    removeIdeaButton.pack(side=tk.LEFT)

def removeModifier(ideaNum):
    if len(ideas[ideaNum]) > 0:
        modifier = ideas[ideaNum].pop()
        modifier.destroy()

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("300x600")
    window.title("Idea Set Geneator")

    menubar = tk.Menu(window)
    fileMenu = tk.Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Save")
    fileMenu.add_separator()
    fileMenu.add_command(label="Set Destination File")
    fileMenu.add_command(label="Load Modifiers", command=(lambda : loadModifiers(fd.askopenfilename())))
    fileMenu.add_command(label="Load Modifier Icons")
    menubar.add_cascade(label="File", menu=fileMenu)
    window.config(menu=menubar)

    tagPanel = createTagPanel(window)
    traditions = createIdeaSection(window, "Tradition(s):", 0)
    idea1 = createIdeaSection(window, "Idea One:", 1)
    idea2 = createIdeaSection(window, "Idea Two:", 2)
    idea3 = createIdeaSection(window, "Idea Three:", 3)
    idea4 = createIdeaSection(window, "Idea Four:", 4)
    idea5 = createIdeaSection(window, "Idea Five:", 5)
    idea6 = createIdeaSection(window, "Idea Six:", 6)
    idea7 = createIdeaSection(window, "Idea Seven:", 7)
    ambition = createIdeaSection(window, "Ambition(s):", 8)
    window.mainloop()