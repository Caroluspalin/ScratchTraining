import java.util.Scanner;

public class Message {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String mail;
        String name;
        String email;

        System.out.print("Syötä sähköpostisi: ");
        mail = scanner.nextLine();

        System.out.printf("Syöttämäsi sähköposti on %s \n", mail);


        if ( !mail.isEmpty() && mail.contains("@") ) {

            name = mail.substring(0, mail.indexOf("@"));
            email = mail.substring(mail.indexOf("@" + 1));
            

            System.out.printf("Sinun käyttäjänimesi: %s \n", name);
            System.out.printf("Sinun mail tunnuksesi on %s \n", email);
        }

        else {

            System.out.println("syöttämäsi sähköposti on virheellinen, tai ei sisällä @ merkkiä syöttösi" + mail);
        }

        scanner.close();
    
        

    }
}