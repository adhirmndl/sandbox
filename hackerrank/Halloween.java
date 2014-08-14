import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Halloween {

 public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int _a;
        _a = in.nextInt();
        long input;
        for (int i = 0; i < _a ; i++ ) {
            input = in.nextLong();
           System.out.println((long)input/2 * ((long)input - (long)input/2)) ;
        }
   }
}
