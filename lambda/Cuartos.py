descripcionCuartos=[
    "Estas en un cuarto oscuro, hay poca luz, no puedes ver mucho, solo hay dos caja pero sin nada interesante.",
    "Estas en un cuarto mas iluminado, hay muchas celdas y encuentras un cofre con cosas muy valiosas.",
    "Estas en un cuarto con antorchas poco iluminado no alcanzas a ver muy bien pero encuentras unas cajas.",
    "Estas en un cuarto muy obscuro no alcanzas a ver nada pero descubriste que hay una espada.",
    "Estas en un cuarto iluminado alcanzas a ver que hay varias celdas pero nada interesante.",
    "Estas en un cuarto obscuro no alcanzas a ver nada pero escuchas sonidos de monstruos.",
    "Estas en una habitación iluminada ves muchas camas hay cajas pero no tienen nada interesante.",
    "Estas en cocina esta un poco iluminada alcanzas a ver un poco de comida y otras cosas.",
    "Estas en una habitación con antorchas con poca iluminación con camas y cajas alcanzas a ver un cofre pero no tiene nada.",
    "Estas en un habitación poco iluminado pero alcanzas a ver que hay trampas pero al final alcanzas a ver un cofre.",
    "Estas en un cuarto poco iluminado no hay nada interesante ves unas cajas pero no tienen nada.",
    "Estas en un sótano esta muy obscuro pero alcanzas a ver algunos cofres con cosas interesantes.",
    "Estas en una biblioteca no hay mucha luz.",
    "Estas en una habitación con antorchas hay unas cajas pero no hay nada.",
    "Estas en un cuarto iluminado no hay nada pero escuchas sonidos de monstruos."
]

valPuertas=0
descripcion=""
puertas=[False,False,False,False]
esSalida=False
valA=True

class Cuarto:
    
    def __init__(self,initVal):
        self.esSalida=False
        valPuertas=initVal;
        valA=True


    def setValPuertas(nuevoVal):
        if valA!=True:
            descripcion=descripcionCuartos[((valPuertas+1)*220%15)]
            valA=False
        valPuertas=valPuertas|nuevoVal

    def darPuertas():
        norte=valPuertas&1
        este=valPuertas&2
        sur=valPuertas&4
        oeste=valPuertas&8

        if norte==1:
            puertas[0]=True

        if este==2:
            puertas[1]=True

        if sur==4:
            puertas[2]=True

        if oeste==8:
            puertas[3]=True

        

    def describirCuarto():
        puertaN=""
        puertaE=""
        puertaS=""
        puertaO=""
        if puertas[0] :
            puertaN="Tienes una puerta al norte.";

        if puertas[1]:
            puertaE="Tienes una puerta al este.";
    
        if puertas[2]:
            puertaS="Tienes una puerta al sur.";

        if puertas[3]:
            puertaO="Tienes una puerta al oeste.";
        
        descrip=descripcion+"Elige una direccion:"+puertaN+puertaE+puertaS+puertaO;

        return descrip;

    def getValPuertas():
        return valPuertas

    def getEsSalida():
        return esSalida

    def setEsSalida(salida):
        esSalida=salida

    def puertaValida(opcion):
        if opcion<4 and opcion>=0:
            return puertas[opcion]
        else:
            return False;