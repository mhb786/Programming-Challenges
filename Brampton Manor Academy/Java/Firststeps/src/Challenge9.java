public class Challenge9 {
    public static void main(String[] args) {

        int n, b, sum = 0;

        for (int i = 1; i<=1000; i++) {

            n = i;
            while (n > 0) {
                b = n%10;
                sum += Math.pow(b, 3);
                n = n/10;
            }

            if (i == sum) {
                System.out.println(i);
            }

            sum = 0;

        }

    }
}