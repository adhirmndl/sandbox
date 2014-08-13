import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ServiceLane {

 public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int _a;
        _a = in.nextInt();
        int _b;
        _b = in.nextInt();
     int[] N = new int[_a];
     for(int i = 0; i < _a; i++)
         N[i] = in.nextInt();
     for(int i = 0; i < _b; i++){
        int _i = in.nextInt();
        int _j = in.nextInt();
         int max = 3;
         for(int k = _i; k <= _j; k++)
             if(N[k] < max)
                max = N[k];
         System.out.println(max);
     }        
   }
}