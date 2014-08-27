import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ChocolateFeast {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i = 0; i < t; i++){
            System.out.println(Solve(in.nextInt(), in.nextInt(), in.nextInt()));
        }
    }
    
    private static long Solve(int N, int C, int M){
        
         //Write code to solve each of the test over here

    	int chocs = N/C;
    	int wraps = N/C;
    	int newChocs = 0;
    	while (wraps >= M){
    		newChocs = wraps/M;
    		chocs += newChocs;
    		wraps = wraps%M + newChocs;
    	}

    	return chocs;
    }
    
    
}
