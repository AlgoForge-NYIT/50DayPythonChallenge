public class Rotation {

    public static void main(String[] args) {
        System.out.println(checkRotation("abcd","dcba"));
    }

    public static boolean checkRotation(String src, String tar){
        // abcd --  length = 4, 0-4
        if(src.length() != tar.length()) return false;
        // 1. duplicate the source string
        String temp = src + src;
        // 2. Check the target by the length:
        int end = src.length();
        int init = 0;
        while(end < temp.length()){
            if(temp.substring(init, end).equals(tar)) return true;
            end ++;
            init ++;
        }
        return false;
    }
}
