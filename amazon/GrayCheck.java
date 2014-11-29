// IMPORT LIBRARY PACKAGES NEEDED BY YOUR PROGRAM
// SOME CLASSES WITHIN A PACKAGE MAY BE RESTRICTED
// DEFINE ANY CLASS AND METHOD NEEDED
// CLASS BEGINS, THIS CLASS IS REQUIRED
public class GrayCheck
{
 //METHOD SIGNATURE BEGINS, THIS METHOD IS REQUIRED
 public static int grayCheck(byte term1, byte term2){
  // INSERT YOUR CODE HERE
  byte xorValue = (byte)(term1^term2);
  // System.out.println(term1 + " " + term2 + " " + xorValue);
  byte check;
  int returnVal = 0;

  for (int i = 0; i < 8; i++){
    check = (byte) (1<<i);
    System.out.println(check);
    if (xorValue == check){
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
      // PLEASE DO NOT MODIFY THIS FUNCTION
      // YOUR FUNCTION SHALL BE AUTOMATICALLY CALLED AND THE INPUTS FROM HERE SHALL BE PASSED TO IT
      byte term1=(byte)0x0a,term2=(byte)0x80;
      int out;
      // ASSUME INPUTS HAVE ALREADY BEEN TAKEN
      out = grayCheck(term1,term2);
      // System.out.println(out);
      //Print the output
 }
}