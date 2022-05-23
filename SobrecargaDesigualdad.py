class SobrecargaDesi:

  """
  SOBRECARGADE DE OPERADORES
  """


  __edad = int(0)
  __antiguedad = int(0)
  __resultado = bool()

  def __init__(self, antiguedad,edad,resultado):
      self.__edad = edad
      self.__antiguedad =antiguedad
      self.__resultado = resultado


  def __str__(self):
      return " La persona con  " + str(self.__antiguedad) + " EDAD " + " ANTIGUEDAD "+ str(self.__edad) + str(self.__resultado)

  def Desigual(self, edad, antiguedad):
      self.__edad = edad
      self.__antiguedad = antiguedad

      if self.__edad >= 60 & self.__antiguedad <= 25:
          self.__jubilacion1 = ("PERTENECE A LA PRIMERA JUBILACION")

      elif self.__edad <= 60 & self.__antiguedad >= 25:
          self.__jubilaciion2 = ("PERTENECE A LA SEGUNDA JUBILACION")

      else:
          self.__edad <= 60 & self.__antiguedad <= 25
          self.__jubilaciion3 = ("PERTENECE A LA TERCERA JUBILACION ")





