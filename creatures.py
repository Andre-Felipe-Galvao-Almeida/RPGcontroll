class Creture():
    def __init__(self):
        self.__atributes = ()
        self.HP = 50
        self.AC = 20

        self.Attack = attack()

    @property
    def atributes(self):
        return self.__atributes

    @atributes.setter
    def atributes(self, atributes):
        if len(atributes) != 6:
            raise Exception("atributes parameter must have 6 values")

        self.__atributes = atributes

    #def SetAttack(self):
        

class attack():
    def __init__(self, touch=False):
        
        self.BonusAttack = 0
        self.dices = "2d6"
        self.BonusDamage = 0

        self.savingThrow = "Reflexo" * touch

jão = Creture()
jão.atributes = ((0,0,0,0,0))