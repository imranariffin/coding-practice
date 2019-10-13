class MyQueue {
    Stack<Integer> mainStack = new Stack<>();
    Stack<Integer> bufferStack = new Stack<>();
    
    // Push element x to the back of queue.
    public void push(int x) {
        mainStack.push(x);
    }

    // Removes the element from in front of queue.
    public void pop() {
        while (!mainStack.empty()) {
            bufferStack.push(mainStack.pop());
        }
        
        bufferStack.pop();
        
        while (!bufferStack.empty()) {
            mainStack.push(bufferStack.pop());
        }
    }

    // Get the front element.
    public int peek() {
        while (!mainStack.empty()) {
            bufferStack.push(mainStack.pop());
        }
        
        int p = bufferStack.peek();
        
        while (!bufferStack.empty()) {
            mainStack.push(bufferStack.pop());
        }
        
        return p;
    }

    // Return whether the queue is empty.
    public boolean empty() {
        return mainStack.empty();
    }
}
