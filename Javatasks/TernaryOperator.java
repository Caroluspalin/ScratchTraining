public class TernaryOperator {
    public static void main(String[] args) {
        
        double taxbracket;
        int income;

        income = 100000;

        taxbracket = (income >= 50000) ? 0.25 : 15;

        System.out.println(income * ( 1 - taxbracket));


    }
}
        