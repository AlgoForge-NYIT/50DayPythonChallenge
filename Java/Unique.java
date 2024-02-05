import java.util.Arrays;

public class Unique {
    public static void main(String[] args) {
        System.out.println(checkUnique("abc"));
    }

    public static boolean checkUnique(String src){
        // [a][b][b][c], length 4, loop 3 times, so length - 1
        char[] array = src.toCharArray();
        Arrays.sort(array);
        for(int i = 0; i < array.length - 1; i++){
            if(array[i] == array[i+1]){
                return false;
            }
        }
        return true;
    }
}
