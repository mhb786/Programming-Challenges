public class Challenge10 {

    public static void main(String[] args) {
        int maxNumber = Integer.parseInt(args[0]);
        int previousNumber = 1;
        int nextNumber = 1;

        System.out.println("Fibonacci Sequence: ");

        for (int i = 1; i <= maxNumber; ++i) {

            System.out.println(previousNumber);

            int sum = previousNumber + nextNumber;
            previousNumber = nextNumber;
            nextNumber = sum;
        }
    }

}