from proyectoj import*
from ClaseDesigualdad import AbsDesi
from SobrecargaDesigualdad import SobrecargaDesi

def main():

   #Llamada a la clase abstracta
  print(AbsDesi.Desigualdades.clasejubilacion(25,45))


    #llamada al metodo de clase
  print(Desigualdades.clasejubilacion(255,45))
  print("")

  Jubilacion1 = SobrecargaDesi(52,14, " corresponde a la jubilacion1  ")
  Jubilacion2 = SobrecargaDesi(20,45, " corresponde a la jubilacion2 ")
  Jubilacin3 = SobrecargaDesi(13,22," corresponde a la jubiacion3 ")
  print(Jubilacion1)
  print(Jubilacion2)
  print(Jubilacin3)


    #llamada al metodo constructor e instnacia
  Desi = Desigualdades(25,45)
     #LLAMADA DEL METODO DE INSTANCIA
  print(Desi.desigualdad1(25,45))


if __name__ == "__main__":
    main()