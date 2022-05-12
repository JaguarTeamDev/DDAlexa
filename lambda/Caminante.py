maxX=0
maxY=0
posX=0
posY=0
dataX=[]
dataY=[]
direc=[]


class Caminante:
    def __init__(self,x,y):
        maxX=x
        maxY=y
        posX=0
        posY=0

    def mover(dir,pasos):
        posXant=posX
        posYant=posY

        if dir==0 and posX-pasos<=0:
            posX=0
        else:
            posX-=pasos

        if dir==1 and posY+pasos>=maxY:
            posY=maxY-1
        else:
            posY+=pasos

        if dir==2 and posX+pasos>=maxX:
            posX=maxX-1
        else:
            posX+=pasos

        if  dir==3 and posY-pasos<=0:
            posY=0
        else:
            posY-=pasos
        
        if posX!=posXant or posY!=posYant:
            dataX.append(posX);
            dataY.append(posY);
            direc.append(dir);

    def recorrerMapa(self):
        for i in range(maxX*maxY):
            if (posY)%2==0:
                self.mover(posX&3,posY)
            else:
                self.mover(posY&3,posX)
                
    def getDataX():
        return dataX

    def getDataY():
        return dataY

    def getDataDirec():
        return direc