import java.util.Deque;
import java.util.ArrayDeque;
import java.lang.Math;

public class MinStack {
	private Deque<Node> stack;

	/** initialize your data structure here. */
	public MinStack() {
		this.stack = new ArrayDeque<Node>();
	}

	public void push(int x) {
		int min = this.stack.isEmpty()? x : Math.min(stack.peek().min, x);
		this.stack.push(new Node(x, min));
	}

	public void pop() {
		this.stack.pop();
	}

	public int top() {
		return this.stack.peek().val;
	}

	public int getMin() {
		return this.stack.peek().min;
	}

	private class Node {
		public int val;
		public int min;

		public Node(int val, int min) {
			this.val = val;
			this.min = Math.min(min, val);
		}
	}

	public static void main(String[] args) {
		MinStack minStack = new MinStack();
		minStack.push(-2);
		minStack.push(0);
		minStack.push(-3);
		System.out.println(minStack.getMin()); // -3
		minStack.pop();
		System.out.println(minStack.top()); // 0
		System.out.println(minStack.getMin());   // -2.
	}
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */