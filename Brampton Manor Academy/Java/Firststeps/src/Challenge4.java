public class Challenge4 {
    public static void main(String[] args) {

        int num = Integer.parseInt(args[0]);
        int result = 1;

        for (int i = 1; i <= num; i++)
            result *= i;

        System.out.println(result);
    }
}