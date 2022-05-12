import Caminante
import Mazmorra
import Jugador
ptrX=0
ptrY=0
xMax=0
yMax=0
maxX=0
maxY=0
puertas=[1,2,4,8];
caminante=Caminante
#mazmorra=Mazmorra
jugador=Jugador
mapa=[[]]
descripcion=""

class Juego():
    def __init__(self,x,y):
        #estos son posiciones que sirven como punteros a los cuartos
        ptrX=0
        ptrY=0
        #estos sirven para definir el valor de la hacion mas lejana
        #donde paso el caminante
        xMax=0
        yMax=0
        #estor sirven para saber el tamaño maximo de la mazmorra
        maxX=x
        maxY=y
        #Instanciamos a nuestros actores
        #caminante=Caminante(maxX,maxY)
        #mazmorra=Mazmorra(maxX,maxY)
        #jugador=Jugador(0,0)
        #iniciamos a los actores
        #caminante.recorrerMapa()
        #mapa=mazmorra.getMap()
        #datos a enviar a la alexa
        descripcion=""

    def modMapa(dir,xant,yant,x,y):

        if dir==0:
            mapa[xant][yant].setValPuertas(1)
            mapa[x][y].setValPuertas(4)
        elif dir==1:
            mapa[xant][yant].setValPuertas(2)
            mapa[x][y].setValPuertas(8)
        elif dir==2:
            mapa[xant][yant].setValPuertas(4)
            mapa[x][y].setValPuertas(1)
        elif dir==3:
            mapa[xant][yant].setValPuertas(8)
            mapa[x][y].setValPuertas(2)
    
    def genCuartos(self):
        x=caminante.getDataX();
        y=caminante.getDataY();
        dir=caminante.getDataDirec();
        ptrXant=0
        ptrYant=0

        while x[0]!=None and y[0]!=None and dir[0]!=None:
            while ptrX!=x[0] or ptrY!=y[0]:
                ptrXant=ptrX;
                ptrYant=ptrY;

                if ptrX>x[0]:
                    ptrX-=1
                
                elif ptrX<x[0]:
                    ptrX+=1

                if ptrY>y[0]:
                    ptrY-=1
                
                elif ptrY<y[0]:
                    ptrY+=1

                if ptrX*ptrY>xMax*yMax:
                    xMax=ptrX
                    yMax=ptrY
                
                self.modMapa(dir[0],ptrXant,ptrYant,ptrX,ptrY)
            x.remove(x[0])
            y.remove(y[0])
            dir.remove(dir[0])
        mapa[xMax][yMax].setEsSalida(True)

    def moverJugador(direccion):
        if direccion==0 and jugador.getPostX()<=0:
            jugador.setPostX(0)
        else:
            jugador.setPostX(jugador.getPostX()-1)

        if direccion==1 and jugador.getPostY()>=maxY:
            jugador.setPostY(maxY-1)
        else:
            jugador.setPostY(jugador.getPostY()+1)

        if direccion==2 and jugador.getPostX()>=maxX:
            jugador.setPostX(maxX-1)
        else:
            jugador.setPostX(jugador.getPostX()+1)

        if direccion==3 and jugador.getPostY()<=0:
            jugador.setPostY(0)
        else:
            jugador.setPostY(jugador.getPostY()-1)
        
    def getDescripcion():
        if mapa[jugador.getPostX()][jugador.getPostY()].getEsSalida()==False:
            return mapa[jugador.getPostX()][jugador.getPostY()].describirCuarto()
        else:
            return "Felecidades, saliste de la mazmorra"