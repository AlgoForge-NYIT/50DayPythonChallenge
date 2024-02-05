import java.util.LinkedList;

public class ListSum {

    public static void main(String[] args) {
        LinkedList<Integer> a = new LinkedList<>();
        a.add(1);
        a.add(2);
        LinkedList<Integer> b = new LinkedList<>();
        b.add(3);
        b.add(4);
        System.out.println(reverseSum(a,b));
    }

    public static double checkSum(LinkedList<Integer> a, LinkedList<Integer> b){
        double first = 0;
        double second = 0;
        double count = 0;

        while(a.peek() != null){
            first += a.pop() * Math.pow(10,count);
            count++;
        }
        System.out.println(first);

        // update the count
        count = 0;
        while(b.peek() != null){
            second += b.pop() * Math.pow(10,count);
            count++;
        }
        System.out.println(second);

        return first + second;
    }

    public static double reverseSum(LinkedList<Integer> a, LinkedList<Integer> b){
        double first = 0;
        double second = 0;
        double count = a.size() - 1;
        while(a.peek() != null){
            first += a.pop() * Math.pow(10,count);
            count--;
        }
        System.out.println(first);

        count = b.size() - 1;
        while(b.peek() != null){
            second += b.pop() * Math.pow(10,count);
            count--;
        }
        System.out.println(second);
        return first + second;
    }
}
