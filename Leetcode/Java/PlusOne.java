public class PlusOne {
    public int[] plusOne(int[] digits) {
        int position = digits.length - 1;
        for(int i = digits.length - 1; i >= 0; i--){
            if(digits[i] < 9){
                break;
            }else{
                position--;
            }
        }

        if(position < 0){
            int[] result = new int[digits.length + 1];
            result[0] = 1;
            return result;
        }else{
            digits[position] += 1;
            for(int i = position + 1; i < digits.length; i++){
                digits[i] = 0;
            }
            return digits;
        }

    }
}
