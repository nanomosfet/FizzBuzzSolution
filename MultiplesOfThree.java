import java.util.*;
public class MultiplesOfThree {

	public static void main(String[] args)
	{
		ArrayList<Integer> multofThree = new ArrayList<Integer>();
		
		int totalNums = Integer.parseInt(args[0]);
		for (int i = 0; i < totalNums; i++)
		{
			if(isMultipleOfThreeOrFive(i)) {
				multofThree.add(i);
				
			}
		}
		System.out.print("Answer is " + sumArray(multofThree));
	}
	
	private static boolean isMultipleOfThreeOrFive(int num)
	{
		if((num%3 == 0 || num%5 == 0) && num != 0)
			return true;
		else
			return false;
		
	}
	
	private static int sumArray(ArrayList<Integer> intArray) 
	{
		int res = 0;
		for (int num : intArray)
			res += num;
		return res;
		
	}
	

}