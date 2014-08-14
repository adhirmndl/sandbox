import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class GameOfThronesI {

 public static void main(String[] args) {
        Scanner myScan = new Scanner(System.in);
        String inputString = myScan.nextLine();
        String ans;


        
            char[] inputArr = inputString.toCharArray();
            Arrays.sort(inputArr);
            inputString = new String(inputArr);
            // System.out.println(inputString);
            ans = "YES";
            boolean once = false;
            for(int i = 0; i < inputArr.length; i+=2){
                if(i + 1 < inputArr.length)
                if(inputArr[i] != inputArr[i+1]){
                    if(once == true){
                        ans = "NO";
                        break;
                    } else{
                        once = true;
                        i++;
                    }
                }
            }
        


        // Assign ans a value of s or no, depending on whether or not inputString satisfies the required condition
        System.out.println(ans);
        myScan.close();
    }
}
