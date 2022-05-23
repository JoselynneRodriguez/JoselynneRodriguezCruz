package Desigualdad;

  /* DESCRIPCION DEL PROBLEMA
El IMSS necesita clasificar a las personas que se jubilarán este año.
Existen tres tipos de jubilaciones: por edad, por antigüedad joven y por
antigüedad adulta. Las personas adscritas a la jubilación por edad deben
tener 60 años o más y una antigüedad en su empleo de menos de 25 años.
Las personas adscritas a la jubilación por antigüedad joven deben tener
menos de 60 años y una antigüedad en su empleo de 25 años o más. Las
personas adscritas a la jubilación por antigüedad adulta deben tener 60
años o más y una antigüedad en su empleo de 25 años o más. Determinar
en qué tipo de jubilación quedará adscrita una persona.

 AUTORA JOSELYNNE RODRIGUEZ CRUZ
   */

 public class Desigualdades {

     //ATRIBUTOS
     private float edad = 0;
     private float antiguedad = 0;


     //METODO CONSTRUCTOR
     public Desigualdades(float edad, float antiguedad) {
         if (edad >= 60 & antiguedad < 25) {
             System.out.println("Corresponde a la Jubilacion1");
         } else if (edad < 60 & antiguedad >25 ){
             System.out.println("Corresponde a la Jubilacion2");
         }else if  (edad >=60 & antiguedad >=25){
             System.out.println("Corresponde a la Jubilacion3");
         }
     }

     //getters
     public  float getEdad(){
         return edad;
         }

     public  float getAntiguedad() {

         return antiguedad;
     }

     //METODO DE INSTANCIA
     public boolean Desigualdad() {
         this.edad = edad;
         this.antiguedad = antiguedad;


         if (this.edad >= 60 & this.antiguedad < 25) {
             System.out.println("Corresponde a la Jubilacion1");

         } else if (this.edad < 60 & this.antiguedad > 25) {
             System.out.println("Corresponde a la Jubilacion2");

         } else if (this.edad >= 60 & this.antiguedad >= 25) {
             System.out.println("Corresponde a la Jubilacion3");

         }
         return Desigualdad();
     }

     //METODO DE CLASE
     public boolean Desigualdado() {
         this.edad = edad;
         this.antiguedad = antiguedad;


         if (this.edad >= 60 & this.antiguedad < 25) {
             System.out.println("Corresponde a la Jubilacion1");

         } else if (this.edad < 60 & this.antiguedad > 25) {
             System.out.println("Corresponde a la Jubilacion2");

         } else if (this.edad >= 60 & this.antiguedad >= 25) {
             System.out.println("Corresponde a la Jubilacion3");

         }
         return Desigualdado();
     }





 }