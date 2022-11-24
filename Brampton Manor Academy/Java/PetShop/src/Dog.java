public class Dog extends Animal{

    private String breed;

    public Dog() {
        name = "default";
        age = 0;
    }

    public Dog (String a, String b, int c) {
        name = a;
        breed = b;
        age = c;

    }

    public String getBreed() {
        return breed;
    }

    public void bark() {
        System.out.println(name + ": Woof!");
    }

    public void EatBiscuit() {
        System.out.println(name + ": Yum!");
    }
}
