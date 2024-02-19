import java.util.ArrayList;
import java.util.List;

public class PascalTriangle {
    public List<List<Integer>> generate(int numRows) {

        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(numRows < 3){
            for(int i = 1; i <= numRows; i++){
                List<Integer> element = new ArrayList<Integer>();
                for(int j = 1; j <= i; j++){
                    element.add(1);
                }
                result.add(element);
            }
            return result;
        }
        // row >= 3:
        for(int i = 1; i <= 2; i++){
            List<Integer> element = new ArrayList<Integer>();
            for(int j = 1; j <= i; j++){
                element.add(1);
            }
            result.add(element);
        }
        int num = 0;
        List<Integer> lastRow;
        for(int i = 2; i < numRows; i++){
            List<Integer> element = new ArrayList<Integer>();
            // insert the first 1:
            element.add(1);
            lastRow = result.get(i-1);
            for(int j = 1; j < i; j++){
                // plug the sum of digits from the last array:
                num = lastRow.get(j-1) + lastRow.get(j);
                element.add(num);
            }
            // insert the last 1:
            element.add(1);
            result.add(element);
        }
        return result;
    }
}
