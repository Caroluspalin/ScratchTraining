import java.util.Scanner;
import java.util.Random;

public class NumberGuess {
    public static void main(String[] args) {

        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        int guess;
        int attempts = 0;
        int min;
        int max;

        System.out.println("Welcome to Number Guessing game");
        System.out.println("First you will choose your min and max number where youre going to guess between");

        System.out.print("Enter min: ");
        min = scanner.nextInt();

        System.out.print("Enter your max ");
        max = scanner.nextInt();

        int randomNumber = random.nextInt(min, max + 1);

        do {
           System.out.print("Enter your guess: ");
           guess = scanner.nextInt();
           attempts++;

            if (guess < randomNumber) {
                System.out.println("Your guess was too low, Try again!");
            }
            else if(guess > randomNumber) {
                System.out.println("Your guess was too high, Try again!");
            }
            else {
                System.out.println("Your guess was CORRECT, you won!");
                System.out.println("Number of attempts " + attempts);
            }

        } while(guess != randomNumber);

        scanner.close();
        
    }
    
}
