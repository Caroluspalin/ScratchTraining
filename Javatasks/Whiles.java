import java.util.Scanner;

public class Whiles {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);

        String name = "";
        int age = 0;
        Boolean student = false;

        while(name.isEmpty()) {
            System.out.print("Enter your name: ");
            name = scanner.nextLine();
        }

        System.out.println("Your name is " + name);

        do {
            System.out.print("Enter your age: ");
            age = scanner.nextInt() ;
        } while (age < 0 || age > 120);
        
        System.out.println("your age is " + age);

        if (student) {
            System.out.println("You are a student");
        }
        else {
            System.out.println("You are not a student");
        }

        System.out.println("you are a student");

        scanner.close();
    }
    
}
