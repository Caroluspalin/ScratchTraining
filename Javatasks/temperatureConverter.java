import java.util.Scanner;

public class temperatureConverter {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        double temp;
        double newTemp;
        String unit;

        
        System.out.print("Input the temperature: ");
        temp = scanner.nextDouble();

        System.out.print("Enter the unit you want to convert to, Celsius or Fahrenheit (c or f )");
        unit = scanner.next().toUpperCase();

        if (unit.contains("C") || unit.contains("F")){
            unit = "°" + unit;
        }
        else {
            System.out.println("The unit wasnt correct");
        }


        newTemp = (unit.contains("C")) ?   (temp - 32) * 5 / 9 : (temp * 9 / 5 ) + 32;


        System.out.printf("%.1f%s", newTemp, unit);

        scanner.close();

    

    
    }
}