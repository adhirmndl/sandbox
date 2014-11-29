import java.util.Scanner;
// IMPORT LIBRARY PACKAGES NEEDED BY YOUR PROGRAM
// SOME CLASSES WITHIN A PACKAGE MAY BE RESTRICTED
// DEFINE ANY CLASS AND METHOD NEEDED
// CLASS BEGINS, THIS CLASS IS REQUIRED
public class SameReflection
{
 //METHOD SIGNATURE BEGINS, THIS METHOD IS REQUIRED
  public static int isSameReflection(String word1, String word2){
    // Check whether word1 and word2 have same reflection.
    // Return 1 or -1
    // INSERT YOUR CODE HERE
    //word1 is reference
    //word2 will be rotated time and again to get right rotations
    //simple wrong edge case: length mismatch
    if (word1.length() != word2.length())
        return -1;
    //simple correct case: equal strings
    if (word1.equals(word2))
        return 1;
        
    int returnVal = -1;
    StringBuilder rotatedw2 = new StringBuilder(word2);
    char firstCh;
    for (int i = 0; i < word1.length(); i++){
        firstCh = rotatedw2.charAt(0);
        rotatedw2 = rotatedw2.delete(0,1).append(firstCh);
        if (rotatedw2.toString().equals(word1)){
            returnVal = 1;
            break;
        }
    }
    return returnVal;
  } 
// METHOD SIGNATURE ENDS

// DO NOT IMPLEMENT THE main( ) METHOD
  public static void main(String[] args)
  {
    String word1,word2;
    // PLEASE DO NOT MODIFY THIS FUNCTION
    Scanner s= new Scanner(System.in);
    word1=s.next();
    word2=s.next();
    // ASSUME INPUTS HAVE ALREADY BEEN TAKEN
    System.out.println(isSameReflection(word1,word2));
  }
}