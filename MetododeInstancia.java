package InstanciaMetodo;
import Desigualdad.Desigualdades;

public class MetododeInstancia {

    private float edad = 0;
    private float antiguedad = 0;


    public boolean Desigualdado() {
        this.edad = edad;
        this.antiguedad = antiguedad;


        if (this.edad >= 60 & this.antiguedad < 25) {
            System.out.println("Corresponde a la Jubilacion1");

        } else if (this.edad < 60 & this.antiguedad > 25) {
            System.out.println("Corresponde a la Jubilacion2");

        } else if (this.edad == 0) {
            System.out.println("Corresponde a la Jubilacion3");

        }
        return Desigualdado();
    }

    public static void  main(String[] args){
        Desigualdades Desigualdades = new Desigualdades(35,45);
        System.out.println(Desigualdades.Desigualdad());

    }


}
