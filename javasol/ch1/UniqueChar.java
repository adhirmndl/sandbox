//package java.chap1;

public class UniqueChar{
		public static void main(String[] args){
			UniqueChar uc = new UniqueChar();

			System.out.println(uc.hasUniqueChars(args[0].toCharArray()));
		}

		public boolean hasUniqueChars(char[] input){
				boolean[] unicode = new boolean[256];
				for(int i = 0; i < input.length; i++)
				{
						if(unicode[input[i]] == true)
								return false;
						unicode[input[i]] = true;
				}
				return true;
		}
}
