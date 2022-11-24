public class Cat extends Animal{

    private String breed;

    public Cat() {
        name = "default";
        age = 0;
    }

    public Cat (String a, String b, int c) {
        name = a;
        breed = b;
        age = c;

    }

    public String getBreed() {
        return breed;
    }

    public void meow() {
        System.out.println(name + " meows");
    }

    public void EatBiscuit() {
        System.out.println(name + ": Yum!");
    }
}

