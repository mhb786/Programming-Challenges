public class Animal {

    protected String name;
    protected int age;

    public Animal() {}

    Animal (String a, int c) {
        name = a;
        age = c;
    }

    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }
    public int getOlder() {
        return age++;
    }

}
