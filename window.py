import customtkinter as ctk
import main

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

        #configuring a screen
        self.title("Auxiliar de Combates para RPG")
        self.geometry(f"{580}x{580}")

        #Round counter frame
        self.roundCounterFrame = ctk.CTkFrame(self)
        self.roundCounterFrame.grid(row=1, column=1)

        self.round = ctk.IntVar(value=1)

        self.PreviousRoundButton = ctk.CTkButton(self.roundCounterFrame, text="prev", command=self.PrevRound, height=25, width=20)
        self.PreviousRoundButton.grid(row=0, column=0)

        self.RoundLabel = ctk.CTkLabel(self.roundCounterFrame, textvariable=self.round)
        self.RoundLabel.grid(row=0, column=1, padx=10)
 

        self.NextRoundButton = ctk.CTkButton(self.roundCounterFrame, text="Next", command=self.NextRound, height=25, width=20)
        self.NextRoundButton.grid(row=0, column=2)

        #creature summary frame
        self.CreatureSummary = ctk.CTkFrame(self)
        self.CreatureSummary.grid(row=0, column=0)

        #hypotenuse calculator
        self.calculatorFrame = ctk.CTkFrame(self)
        self.calculatorFrame.grid(row=0, column=0)

        self.cateto01 = ctk.IntVar()
        self.cateto02 = ctk.IntVar()
        
        self.catetoSubititle01 = ctk.CTkLabel(self.calculatorFrame, text="Cateto 1: ")
        self.catetoSubititle02 = ctk.CTkLabel(self.calculatorFrame, text="Cateto 2: ")

        self.catetoSubititle01.grid(row=0, column=0)
        self.catetoSubititle02.grid(row=1, column=0)

        self.CatetoEntry01 = ctk.CTkEntry(self.calculatorFrame, textvariable=self.cateto01, width=50)
        self.CatetoEntry01.grid(row=0, column=1)

        self.CatetoEntry02 = ctk.CTkEntry(self.calculatorFrame, textvariable=self.cateto02, width=50)
        self.CatetoEntry02.grid(row=1, column=1)

        self.hypotenuseSubtitle = ctk.CTkLabel(self.calculatorFrame, text="Hipotenusa: ")
        self.hypotenuse = ctk.IntVar()
        
        self.CalcButton = ctk.CTkButton(self.calculatorFrame, text="Calcular", command=self.CalcHypotenuse)
        self.CalcButton.grid()

        self.mainloop()
    
    def NextRound(self):
        self.handling = self.round.get() + 1
        self.round.set(self.handling)

    def PrevRound(self):
        if self.round.get() > 0:
            self.handling = self.round.get() - 1
            self.round.set(self.handling)

    def CalcHypotenuse(self):
        self.hypotenuse.set(main.hypotenuse(self.cateto01.get(), self.cateto02.get()))
        

screen = combatUtilities()