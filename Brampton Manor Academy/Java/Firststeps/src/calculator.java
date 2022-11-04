import java.util.Scanner;

public class calculator {

//    public static void main(String[] args) {
//        int num1, num2;
//        Scanner sc = new Scanner(System.in);
//
//        num1 = sc.nextInt();
//        num2 = sc.nextInt();
//    }

    private static int addition (int a, int b) {
        int answer = a + b;
        return answer;
    }

    private static int subtraction (int a, int b) {
        int answer = a - b;
        return answer;
    }

    private static int multiply (int a, int b) {
        int answer = a * b;
        return answer;
    }

    private static int division (int a, int b) {
        int answer = a / b;
        return answer;
    }

    public static void main(String[] args) {
        int num1 = Integer.parseInt(args[0]);
        int num2 = Integer.parseInt(args[1]);

        int answer = multiply(num1, num2);
        System.out.println(answer);
    }


}
