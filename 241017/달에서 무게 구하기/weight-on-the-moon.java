public class Main {
    public static void main(String[] args) {
        int weight = 13;
        double moonGravity = 0.165000;

        System.out.printf(weight + " * ");
        System.out.printf("%.6f" , moonGravity);
        System.out.printf(" = ");
        System.out.printf("%.6f", weight*moonGravity);

    }
}