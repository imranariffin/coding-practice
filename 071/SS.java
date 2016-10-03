public class StringStack {
	LinkedList head;

	public StringStack() {
		head = null;
	}

	public void 
			push(String s) {
		LinkedList e = new LinkedList(s);
		e.next = head;
		head = e;
	}

	public LinkedList
	pop() {
		// if (head == null) throw new EmptyStackException();
		LinkedList ret = head;
		head = head.next;
		return ret;
	}

	public void print() {
		System.out.println(flatten());
	}

	public String
	flatten() {
		LinkedList ptr = head;
		StringBuilder sb = new StringBuilder();
		StringStack rev = new StringStack();
		while (ptr!=null) {
			rev.push(ptr.val);
			ptr = ptr.next;
		}
		LinkedList revPtr = rev.head;
		while (revPtr!=null) {
			// System.out.format("%s ~> ", ptr.val);
			sb.append(revPtr.val);
			revPtr = revPtr.next;
		}

		return sb.toString();
	}
}