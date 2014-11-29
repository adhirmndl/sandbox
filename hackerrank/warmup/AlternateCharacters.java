//AlternateCharacters.java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class AlternateCharacters {

	public static int minDeletions(String input){
		char ch = input.charAt(0);
		int gStringLength = 1;
		for (int i = 1; i < input.length(); i++ ) {
			if (input.charAt(i) != ch){
				ch = input.charAt(i);
				gStringLength++;
			}
		}
		return input.length() - gStringLength;
	}

   
 	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int _a, nDeletions;
        String temp;
        _a = in.nextInt();
        in.nextLine();
        for (int i = 0; i < _a; i++) {
        	temp = in.nextLine(); 	
        	nDeletions = 0;
        	if (temp.length() > 0){
	        	nDeletions = minDeletions(temp);
		        System.out.println(nDeletions);
	    	}
        }
   }
}