import java.util.Arrays;

public class Permutation {

    public static void main(String[] args) {
        System.out.println(checkPermute("abc","bcad"));
    }

    public static boolean checkPermute(String a, String b){
        // 1. convert them to Char Array, then sort both
        char[] stringOne = a.toCharArray();
        Arrays.sort(stringOne);
        char[] stringTwo = b.toCharArray();
        Arrays.sort(stringTwo);

        // 2. convert back to string:
        a = String.valueOf(stringOne);
        b = String.valueOf(stringTwo);

        // 3. compare them:
        return a.equals(b);
    }
}
