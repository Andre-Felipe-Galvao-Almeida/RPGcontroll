from typing import Optional, Tuple, Union
import customtkinter as ctk
from main import *

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")


class creatureScreen(ctk.CTk):
    def __init__(self, creature):
        super().__init__()
        self.creature = creature
        self.title("Auxiliar de Combates para RPG")
        self.geometry(f"{580}x{580}")


        self.MainStatus = ctk.CTkFrame(self)
        self.MainStatus.grid(row=0, column=0)
        self.health = (ctk.CTkLabel(self.MainStatus, text=f"HP: "),
                        ctk.CTkLabel(self.MainStatus, text=self.creature.currentHP),
                        ctk.CTkLabel(self.MainStatus, text=f"/{self.creature.HP}"))
        
        self.health[0].grid(row=0, column=0)
        self.health[1].grid(row=0, column=1)
        self.health[2].grid(row=0, column=2)

        self.ArmourClass = (ctk.CTkLabel(self.MainStatus, text=f"CA: "),
                            ctk.CTkLabel(self.MainStatus, text=self.creature.AC))
        
        self.ArmourClass[0].grid(row=1, column=0)
        self.ArmourClass[1].grid(row=1, column=1)

        self.mainloop()

class combatUtilities(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Auxiliar de Combates para RPG")
        self.geometry(f"{580}x{580}")

        self.roundCounterFrame = ctk.CTkFrame(self)
        self.roundCounterFrame.grid(row=0, column=0)

        self.round = ctk.IntVar(value=1)

        self.PreviousRoundButton = ctk.CTkButton(self.roundCounterFrame, text="prev", command=self.PrevRound)
        self.PreviousRoundButton.grid(row=0, column=0)

        self.RoundLabel = ctk.CTkLabel(self.roundCounterFrame, textvariable=self.round)
        self.RoundLabel.grid(row=0, column=1)

        self.NextRoundButton = ctk.CTkButton(self.roundCounterFrame, text="Next", command=self.NextRound)
        self.NextRoundButton.grid(row=0, column=2)

        self.mainloop()
    
    def NextRound(self):
        self.handling = self.round.get() + 1
        self.round.set(self.handling)

    def PrevRound(self):
        self.handling = self.round.get() - 1
        self.round.set(self.handling)

screen = combatUtilities()