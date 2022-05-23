"""
AUTORA JOSELYNNE RODRIGUEZ CRUZ
 El IMSS necesita clasificar a las personas que se jubilarán este año.
Existen tres tipos de jubilaciones: por edad, por antigüedad joven y por
antigüedad adulta. Las personas adscritas a la jubilación por edad deben
tener 60 años o más y una antigüedad en su empleo de menos de 25 años.
Las personas adscritas a la jubilación por antigüedad joven deben tener
menos de 60 años y una antigüedad en su empleo de 25 años o más. Las
personas adscritas a la jubilación por antigüedad adulta deben tener 60
años o más y una antigüedad en su empleo de 25 años o más. Determinar
en qué tipo de jubilación quedará adscrita una persona.
"""

class Desigualdades:

 #ATRIBUTOS

   __edad = int(0)
   __antiguedad = int(0)

   def __init__(self,edad,antiguedad):
       self.__edad = edad
       self.__antiguedad = antiguedad


   def Desigual(self,edad,antiguedad):

       if self.__edad >= 60 & self.__antiguedad < 25:
           print("PERTENECE A LA PRIMERA JUBILACION")

       elif self.__edad <= 60 & self.__antiguedad >= 25:
           print("PERTENECE A LA SEGUNDA JUBILACION")

       else:
           self.__edad >= 60 & self.__antiguedad >= 25
           print("PERTENECE A LA TERCERA JUBILACION")



    #METODO DESTRUCTOR
   def __del__(self):
       self.__Desigual()
       self.__Desigualdado()




       #METODO DE CLASE
   @classmethod
   def clasejubilacion(cls,edad,antiguedad):
       if (edad >=60 & antiguedad <25):
           print  ("PERTENECE A LA PRIMERA JUBILACION")

       elif  (edad <=60 & antiguedad >=25):
           print ("PERTENECE A LA SEGUNDA JUBILACION")

       else :
           (edad >=60 & antiguedad>=25)
           print ("PERTENECE A LA TERCERA JUBILACION")

    #METODO DE INSTANCIA
   def desigualdad1(self,edad,antiguedad):
       self.__edad = edad
       self.__antiguedad = antiguedad

       if self.__edad >=60 & self.__antiguedad <=25:
           self.__jubilacion1 = ("PERTENECE A LA PRIMERA JUBILACION")

       elif self.__edad <=60 & self.__antiguedad >=25:
           self.__jubilaciion2 = ("PERTENECE A LA SEGUNDA JUBILACION")

       else:
           self.__edad <=60 & self.__antiguedad <=25
           self.__jubilaciion3 = ("PERTENECE A LA TERCERA JUBILACION ")





