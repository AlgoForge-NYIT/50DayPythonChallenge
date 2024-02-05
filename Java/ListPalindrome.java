import java.util.LinkedList;

public class ListPalindrome {
    public static void main(String[] args) {
        LinkedList<String> a = new LinkedList<>();
        a.add("a");
        a.add("b");
        a.add("a");
        a.add("b");
        System.out.println(checkListPalindrome(a));
        // abab -- false
        // aba -- true
    }

    public static boolean checkListPalindrome(LinkedList<String> a){
        // 1. compare first and last
        while(a.size() > 1){
            if(!a.getFirst().equals(a.getLast())){
                return false;
            }
            // 2. remove the first and the last and continue
            a.removeFirst();
            a.removeLast();
        }
        return true;
    }
}
