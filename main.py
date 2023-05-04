# from creatures import *

# class Combat():
#     def __init__(self):
#         self.__round = 0
#         self.figthers = {}
#         self.effects = []

#     def RoundPass(self):
#         self.__round += 1

#     def AddFigther(self, figther):
#         self.figthers.update({figther})
    
#     def RmFigther(self, figther):
#         self.figthers.pop(str(figther))
    
def hypotenuse(A, B):
    sqrA = A*A
    sqrB = B*B

    sqrHyp = sqrA+sqrB

    hyp = sqrHyp**(1/2)

    return hyp