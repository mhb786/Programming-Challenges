import java.util.Scanner;

public class Challenge6 {
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        System.out.println("Enter an integer:");
        int x = s.nextInt();
        String y = Integer.toString(x);

        StringBuilder input = new StringBuilder();
        input.append(y);
        input.reverse();

        System.out.println(input);
    }
}
