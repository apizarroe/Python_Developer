public class HelloUser {
    public static void main(String[] args) {

        String saludo = "Aldo Pizarro Espinoza";
        System.out.println(saludo);
        // Usar soutv(para copiar el comportamiento al printout
        System.out.println("saludo.toUpperCase() = " + saludo.toUpperCase());

        int numero = 11;
        System.out.println("numero = " + numero);

        // Contexto1 (principal)
        /* Si se crea una variable en este contexto
        sera visible en los contextos inferiores */
        boolean valor = true;
        int numero2 = 5;

        if(valor){
            // Contexto2 (if)
            /* Si se crea una variable en este contexto
            no sera visible en el contexto1 */
            System.out.println("numero = " + numero);
        }

        System.out.println("numero2 = " + numero2);

        /* Este tipo de variable fija su tipo de forma automática
        según el tipo de variable que se le asigne */
        var numero3 = 15;
        var numero4 = "15";
        
        String nombre;
        nombre = "Andrés";
        
        if (numero >10){
            nombre = "Juan";
        }

        /* Considerar que la variable debe tener un valor
        antes de ser utilizada, esto se puede forzar mediante
        la inicializacion de la variable */
        System.out.println("nombre = " + nombre);

        /* Las variables puede iniciarse con:
        caracter, "$", "_", seguido de una letra, digito o "$", "_" */
        int $ed4d1 = 5;
        int edad_persona = 5;
        int edadPersona = 5; //Convencion
        //Se recomienda no usar caracteres especiales, ej: ñ, á

    }
}
