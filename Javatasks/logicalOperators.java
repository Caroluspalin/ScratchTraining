import java.util.Scanner;

public class logicalOperators {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);

        String userName;

        System.out.print("Enter your new username: ");
        userName = scanner.nextLine();

        if (userName.length() < 4 || userName.length() > 12) {
            System.out.println("Username must be between 4-12 characters!");
        }
        else if(userName.contains(" ") || userName.contains("_")) {
            System.out.println("Your username cant contain spaces or underscores");
        }
        else {
            System.out.println("Your new username is " + userName);
        }

        scanner.close();

    }
    
}
