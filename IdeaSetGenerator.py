from Stuff.Modifier import Modifier
from Stuff.IdeaModifier import IdeaModifier
import tkinter as tk
from tkinter import filedialog as fd
from os.path import exists
from os import getcwd

DEFAULT_MODIFIERS_FILE = "modifiers.txt"

modifiers = dict()
ideas = [[], [], [], [], [], [], [], [], []]

def loadModifiers(filePath):
    if exists(filePath):
        f = open(filePath, 'r')
        for line in f:
            name, baseValue, description, effectType, versionAdded = line.split(";")
            modifiers[name] = Modifier(name, baseValue, description, effectType, versionAdded)
        for idea in ideas:
            for ideaModifier in idea:
                ideaModifier.updateModifiers(modifiers)
    else:
        tk.messagebox.showinfo("File Not Found", "The following file canot be found: {}".format(filePath))

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

def createIdeaSection(window, title, ideaNum, startingIdeas):
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
    for i in range(0, startingIdeas):
        ideas[ideaNum].append(IdeaModifier(modifiersPanel, modifiers))

def removeModifier(ideaNum):
    if len(ideas[ideaNum]) > 0:
        modifier = ideas[ideaNum].pop()
        modifier.destroy()

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("400x825")
    window.title("Idea Set Geneator")

    loadModifiers("{}/{}".format(getcwd(), DEFAULT_MODIFIERS_FILE))

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
    traditions = createIdeaSection(window, "Tradition(s):", ideaNum=0, startingIdeas=2)
    idea1 = createIdeaSection(window, "Idea One:", ideaNum=1, startingIdeas=1)
    idea2 = createIdeaSection(window, "Idea Two:", ideaNum=2, startingIdeas=1)
    idea3 = createIdeaSection(window, "Idea Three:", ideaNum=3, startingIdeas=1)
    idea4 = createIdeaSection(window, "Idea Four:", ideaNum=4, startingIdeas=1)
    idea5 = createIdeaSection(window, "Idea Five:", ideaNum=5, startingIdeas=1)
    idea6 = createIdeaSection(window, "Idea Six:", ideaNum=6, startingIdeas=1)
    idea7 = createIdeaSection(window, "Idea Seven:", ideaNum=7, startingIdeas=1)
    ambition = createIdeaSection(window, "Ambition(s):", ideaNum=8, startingIdeas=1)
    window.mainloop()