class Creture():
    def __init__(self):
        self.Level = 1
        self.BBA = 1

        self.__atributes = (10, 10, 10, 10, 10, 10)
        
        self.HP = 50
        self.AC = 20
        self.currentHP = 10

        self.Attack = []

        self.status = status()
        self.initiative = object()

    @property
    def atributes(self):
        return self.__atributes

    @atributes.setter
    def atributes(self, atributes):
        if len(atributes) != 6:
            raise Exception("atributes parameter must have 6 values")

        self.__atributes = atributes

    def __str__(self):
        return f"""
        Nivel: {self.Level}
        HP: {self.HP}
        CA: {self.AC}"""
#============================================================================#
#                                SET ATTACKS                                 #

    def SetAttack(self):
        handlingAttack = attack()

        handlingAttack.BonusAttack = self.CalculateBonusAttack()
        handlingAttack.BonusDamage = self.CalculateBonusDamage()

        self.Attack.append(handlingAttack)



    def CalculateBonusAttack(self):

        handlingBonusAttack = int(self.Level * self.BBA) + self.AtributeBonus()
        
        return handlingBonusAttack
    
    def CalculateBonusDamage(self):
        handlingBonusDamage = int(self.Level/2) + self.AtributeBonus()
        
        return handlingBonusDamage
    

#======================================#
#              GET ATRIBUTES           #

    def AtributeBonus(self, Fo=False, De=False, Co=False, In=False, Sa=False, Ca=False):
        handlingAtributes = (Fo, De, Co, In, Sa, Ca)
        atributeBonus = 0

        for atribute in handlingAtributes:
            atributeBonus += ((self.atributes[atribute]-10)/2) * handlingAtributes[atribute]
            
        return atributeBonus

#============================================================================#
#                          CLASS ATTACK & SKILL                              #

class attack():
    def __init__(self, touch=False):
        
        self.BonusAttack = 0
        self.dices = "2d6"
        self.BonusDamage = 0

        self.savingThrow = "Reflexo" * touch

    def __str__(self):
        return f"""
        Ataque: {self.BonusAttack}
        Dano: {self.dices} + {self.BonusDamage}
        """

#============================================================================#
#                               CLASS STATUS                                 #

class status():
    def __init__(self):
        self.attackModifier = 0
        self.damageModifier = 0
        self.armourModifier = 0

#============================================================================#
#                                 INITIATIVE                                 #

class initiative():
    def __init__(self):
        self._LinkedMOB = object()
        self._value = int()

    @property
    def LinkedMOB(self):
        return self._LinkedMOB
    
    @LinkedMOB.setter
    def LinkedMOB(self, mob):
        if isinstance(mob, Creture):
            self._LinkedMOB = mob
        
        else:
            raise Exception("Instance not compatible")
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, newValue):
        if isinstance(newValue, int):
            self._value = newValue

        else:
            raise Exception("Please, initiative needs to be int value")