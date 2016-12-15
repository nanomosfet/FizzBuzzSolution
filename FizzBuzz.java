public class FizzBuzz {
		public static void main(String[] args) {
			for(int i = 0; i <= 100; i++) {
				
				if(multipleOfThree(i))
					System.out.print("Fizz");
				if(multipleOfFive(i))
					System.out.print("Buzz");				
				if(!(multipleOfFive(i) || multipleOfThree(i)))
					System.out.print(i);
				
				if(i != 100)
					System.out.print(" ,");
				
				
			}
		}
		
		private static boolean multipleOfThree (int num) {
			if(num%3 == 0)
				return true;
			else
				return false;
		
		}
		private static boolean multipleOfFive (int num) {
			if(num%5 == 0)
				return true;
			else
				return false;
			
		}
		
		private static boolean isInRange(int num) {
			if(num > 50 || num < 0)
				return false;
			return true;
		}
		
		
		
		
}