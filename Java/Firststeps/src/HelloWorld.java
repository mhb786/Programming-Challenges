public class HelloWorld {
    public static void main(String[] args) {
        for_loop_yes();
        car_loop();
        weekend();
        switch_weekend();
    }

    public static void for_loop_yes() {
        for (int i =0; i < 5; i++) {
            System.out.println("Yes");
        }
    }

    public static void car_loop() {
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};

        for (String car : cars) {
            System.out.println(car);
        }
    }

    public static void weekend() {
        int day = 7;

        if (day == 6) {
            System.out.println("Today is Saturday");
        }
        else if (day == 7) {
            System.out.println("Today is Sunday");
        }
        else {
            System.out.println("Looking forwars to the weekend");
        }
    }

    public static void switch_weekend() {
        int day = 4;

        switch (day) {
            default:
                System.out.println("Looking forward to the weekend");
                break;
            case 6:
                System.out.println("Today is Saturday");
                break;
            case 7:
                System.out.println("Today is Sunday");
                break;
        }
    }
}