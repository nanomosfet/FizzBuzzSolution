public class largestPrimeNumber {
	public static void main(String args[]) {
		double inputNumber = 600851475143d;
		double[] primeFactors = new double[10000]; 
		double factoredOutNumber = inputNumber;
		double curDivider = 2;
		int count = 0;
		double lastFactor = 0;
		while(factoredOutNumber != 1){
			if(factoredOutNumber%curDivider == 0) {
				factoredOutNumber = factoredOutNumber/curDivider;
				primeFactors[count] = curDivider;
				lastFactor = curDivider;
				System.out.println(lastFactor);
			}else{
				curDivider++;
			}
		}

		System.out.print("largestPrimeNumber = "+lastFactor);
		
			
		
	}
	//Returns an array of all the factors in a number
	

	// Takes an input number and checks if it is a prime number with 
	// brute force.
	private static boolean isPrimeNumber(double number) {
		if(number <= 0)
			return false;
		if(number == 1)
			return true;
			
		for (double i = 2; i < number; i++) {			
			if((number%i == 0))
				return false;				
		}
		
		return true;
	}

}