import java.util.*;

public class EvenFibNumbersAdd {
	public static void main(String[] args) {
		int idx = 2;
		int tempFib = 0;
		ArrayList<Integer> evenFibList = new ArrayList<Integer>();
		ArrayList<Integer> FibList = new ArrayList<Integer>();
		//initialize fiblist
		FibList.add(1);
		FibList.add(2);
		
		evenFibList.add(2);
		//populate and 
		while(true) {
			tempFib = FibList.get(idx - 2) + FibList.get(idx - 1);
			idx++;
			if(tempFib >= 4000000)
				break;
			FibList.add(tempFib);
			if(isEven(tempFib))
				evenFibList.add(tempFib);
		}
		
		System.out.print(sumArray(evenFibList));
		
		
		
	}
	
	private static int sumArray(ArrayList<Integer> intArray) 
	{
		int res = 0;
		for (int num : intArray)
			res += num;
		return res;
		
	}
	
	private static boolean isEven(int num) {
		if(num % 2 == 0 && num != 0)
			return true;
		else
			return false;
	}
	
	
}