import java.lang.reflect.Array;
import java.util.Arrays;

public class CapsChanger {
    // Function to generate permutations
    static String[] permute(String input) {
        input = input.toLowerCase();
        int combos = (int) Math.pow(2,input.length());
        String[] permutations = new String[combos];
        for (int i = 0; i < combos; i++) {
            char[] combinations = input.toCharArray();
            for (int j = 0; j < input.length(); j++) {
                if (((i >> j) & 1) == 1) {
                    combinations[j] = Character.toUpperCase(input.charAt(j));
                }
            }
            permutations[i] = new String(combinations);
        }
        System.out.println(Arrays.toString(permutations));
        return permutations;
    }


}
