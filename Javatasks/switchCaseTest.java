import java.util.Scanner;

public class calculator {
    public static void main(String[] args) {

        String paeva;
        
        Scanner scanner = new Scanner(System.in);

        System.out.print("Mikä päivä tänään on: ");
        paeva = scanner.nextLine();

        
        
        switch(paeva) {
            case "Maanantai", "Tiistai", "Keskiviikko", "Torstai" -> System.out.println("On vielä arkiviikko, tsemppiä");
            case "Perjantai" -> System.out.println("Tänään alkaa,nyt vielä töihin");
            case "Lauantai", "Sunnuntai" -> System.out.println("Viikonloppu käynnissä");
            default -> System.out.println("Syöttämäsi päivä ei ole validi");
        }

        scanner.close();
    }
}