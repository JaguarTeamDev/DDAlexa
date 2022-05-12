import Cuartos
sizeX=0
sizeY=0

mapaCuartos=[[]]

class Mazmorra:
    def __init__(self,tamX,tamY):
        sizeX=tamX
        sizeY=tamY

        for i in range(tamX):
            mapaCuartos.append([])
            for j in range(tamY):
                mapaCuartos[i].append(Cuartos.Cuarto(0))
    
    def printMap():
        for i in range(sizeX):
            for j in range(sizeY):
                if mapaCuartos[i][j].getValPuertas()!=0:
                    mapaCuartos[i][j].darPuertas()
                    mapaCuartos[i][j].describirCuarto()