from Stuff.Modifier import Modifier
import tkinter as tk

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

def 

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

def createIdeaSection(window, title):
    panel = tk.PanedWindow(window, orient=tk.VERTICAL)
    panel.pack(side=tk.TOP)
    modifiersList = []
    modifiersPanel = tk.PanedWindow(window, orient=tk.VERTICAL)
    modifiersPanel.pack(side=tk.TOP)
    ideaLabel = tk.Label(panel, text=title)
    ideaLabel.pack(side=tk.LEFT)
    addIdeaButton = tk.Button(panel, text="+", command=(lambda : addModifier(modifiersPanel, modifiersList)))
    addIdeaButton.pack(side=tk.LEFT)
    removeIdeaButton = tk.Button(panel, text="-", command=(lambda : removeModifier(modifiersList)))
    removeIdeaButton.pack(side=tk.LEFT)
    return modifiersList

def addModifier(panel, modifiersList):
    modifierPanel = tk.PanedWindow(panel, orient=tk.VERTICAL)
    modifierPanel.pack(side=tk.TOP)
    #modifierImage = tk.Image(modifierPanel)
    #modifierImage.pack(tk.LEFT)
    modifier = tk.Entry(modifierPanel, width=24)
    modifier.pack(side=tk.LEFT)
    modifiersList.append(modifierPanel)

def removeModifier(modifiersList):
    if len(modifiersList) > 0:
        modifier = modifiersList.pop()
        modifier.destroy()

if __name__ == "__main__":
    f = open("modifiers.txt", 'r')
    modifiers = dict()
    for line in f:
        name, baseValue, description, effectType, versionAdded = line.split(";")
        modifiers["name"] = Modifier(name, baseValue, description, effectType, versionAdded)
    
    window = tk.Tk()
    window.geometry("300x600")
    window.title("Idea Set Geneator")

    menubar = tk.Menu(window)
    fileMenu = tk.Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Save")
    fileMenu.add_separator()
    fileMenu.add_command(label="Set Destination File")
    fileMenu.add_command(label="Load Modifiers")
    fileMenu.add_command(label="Load Modifier Icons")
    menubar.add_cascade(label="File", menu=fileMenu)

    tagPanel = createTagPanel(window)
    traditions = createIdeaSection(window, "Tradition(s):")
    idea1 = createIdeaSection(window, "Idea One:")
    idea2 = createIdeaSection(window, "Idea Two:")
    idea3 = createIdeaSection(window, "Idea Three:")
    idea4 = createIdeaSection(window, "Idea Four:")
    idea5 = createIdeaSection(window, "Idea Five:")
    idea6 = createIdeaSection(window, "Idea Six:")
    idea7 = createIdeaSection(window, "Idea Seven:")
    ambition = createIdeaSection(window, "Ambition(s):")
    window.mainloop()