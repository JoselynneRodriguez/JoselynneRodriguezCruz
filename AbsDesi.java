public  abstract  class AbsDesi {

    public static Boolean jubilacio1(double edad, double antiguedad) {
        Boolean jubilacion1 = edad >= 60 & antiguedad < 25;
        return jubilacion1;
    }

    public  static Boolean jubilacio2(double edad, double antiguedad){
        boolean jubilacion2 = edad <= 60 & antiguedad >= 25;
        return  jubilacion2;
    }

    public static  Boolean jubilaio3 (double edad, double antiguedad){
        boolean jubilacion3 = edad >= 60 & antiguedad >= 25;
        return  jubilacion3;
    }
}