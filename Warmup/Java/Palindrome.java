public class Palindrome {
    public static void main(String[] args) {
        System.out.println(checkPalindrome("abba"));
    }

    public static boolean checkPalindrome(String a){
        // 1. remove all white space:
        a = a.replace(" ","");
        // 2. check the midpoint:
        if((a.length()%2) == 0){
            // this means the string length is even:
            // ex: abbc, abcddcba
            int left = a.length()/2 - 1;
            int right = a.length()/2;
            for(int i = 0; i < a.length()/2; i++){
                if(a.charAt(left) != a.charAt(right)){
                    return false;
                }
            }
            return true;
        }else{
            // this means the string length is odd:
            // ex: abcba
            int left = a.length()/2 - 1;
            int right = a.length()/2 + 1;
            for(int i = 0; i < a.length()/2; i++){
                if(a.charAt(left) != a.charAt(right)){
                    return false;
                }
            }
            return true;
        }
    }
}
