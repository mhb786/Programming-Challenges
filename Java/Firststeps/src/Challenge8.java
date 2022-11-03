public class Challenge8 {
    static int highestfactor(int x, int y) {

        int i, hcf = 0;
        for (i = 1; i <= x || i <= y; i++) {
            if (x % i == 0 && y % i == 0)
                hcf = i;
        }
        return hcf;
    }

    public static void main(String[] args) {
        int result = highestfactor(10, 15);
        System.out.println("The highest common factor is " + result);
    }

}
