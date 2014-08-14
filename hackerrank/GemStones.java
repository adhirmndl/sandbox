import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class GemStones {

 public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int _a;
        _a = in.nextInt();

        int[] gems = new int[26];

        String firstWord = in.next();
        for(int i = 0; i < firstWord.length(); i++)
            gems[firstWord.charAt(i) - 97] = 1;
        // printArray(gems);
        String inputWord;
        for (int i = 0; i < _a -1; i++){
            inputWord = in.next();
            for (int j = 0; j < inputWord.length(); j++){
                if(gems[inputWord.charAt(j) - 97] == i + 1)
                    gems[inputWord.charAt(j) - 97] = i + 2;
            }
        // printArray(gems);
        }

        int count = 0;
        for(int i = 0; i < gems.length; i++)
            if (gems[i] == _a)
                count++;
        System.out.println(count);
   }
}
