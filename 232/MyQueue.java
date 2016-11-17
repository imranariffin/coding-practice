class MyQueue {
    class Stack {
        class Node {
            public int val;
            public Node next;
            public Node(int x) {val = x; next = null;}
        }
        public Node head;
        public Stack() {head = null;}
        public void push(int x) {
            Node node = this.new Node(x);
            node.next = head;
            head = node;
        }
        public int pop() {
            Node ret = head;
            head = head.next;
            return ret.val;
        }
        public boolean empty() {
            return (head == null);
        }
    }
    Stack istack = this.new Stack();
    Stack ostack = this.new Stack();

    // Push element x to the back of queue.
    public void push(int x) {
        istack.push(x);
    }

    // Removes the element from in front of queue.
    public void pop() {
        while (!istack.empty()) {
            ostack.push(istack.pop());
        }
        ostack.pop();
        while (!ostack.empty()) {
            istack.push(ostack.pop());
        }
    }

    // Get the front element.
    public int peek() {
        while (!istack.empty()) {
            ostack.push(istack.pop());
        }
        int ret = ostack.pop();
        ostack.push(ret);
        while (!ostack.empty()) {
            istack.push(ostack.pop());
        }
        return ret;
    }

    // Return whether the queue is empty.
    public boolean empty() {
        return istack.empty();
    }
}