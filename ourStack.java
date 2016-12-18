import java.util.*;

public class ourStack {
	
	private int[] ourList = new int[10];
	
	private int StackPointer = 0;
	
	public void push(int num) {
		if(StackPointer >= 10)
			throw new IndexOutOfBoundsException();
		ourList[StackPointer] = num;
		StackPointer++;
		
	}
	
	public int pop() {
		int res = ourList[StackPointer - 1];
		StackPointer--;
		return res;
	}
	
	
	
	
	public static void main(String[] args) {
		ourStack myStack = new ourStack();
		for (int i = 0; i < 10; i++ )
			myStack.push(i);
		System.out.print(myStack.pop());
		
	}
	
	
}

