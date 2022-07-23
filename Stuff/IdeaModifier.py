import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox

class IdeaModifier:
    def __init__(self, parentPanel, modifiers):
        self.modifierPanel = tk.PanedWindow(parentPanel, orient=tk.VERTICAL)
        self.modifierPanel.pack(side=tk.TOP)
        #modifierImage = tk.Image(modifierPanel)
        #modifierImage.pack(tk.LEFT)
        #modifier = tk.Entry(modifierPanel, width=24)
        #modifier.pack(side=tk.LEFT)
        self.modifierField = AutocompleteCombobox(self.modifierPanel, width=12, completevalues=modifiers)
        self.modifierField.pack(side=tk.LEFT)
        self.modifierAmount = tk.Entry(self.modifierPanel, width=5)
        self.modifierAmount.pack(side=tk.LEFT)

    def destroy(self):
        self.modifierPanel.destroy()
        self.modifierField.destroy()
        self.modifierAmount.destroy()