public class Solution {
    public int findKthLargest(int[] nums, int k) {
        MaxHeap maxHeap = new MaxHeap(100);
        
        for (int i = 0; i < nums.length; i++) {
            maxHeap.insert(nums[i]);
        }
        
        int kVal = -1;
        
        for (int i = 0; i < k; i++) {
            kVal = maxHeap.extract();
        }
        
        return kVal;
    }
    
    public class MaxHeap {
        private int heapSize = 0;
        private int[] A;
        
        public MaxHeap(int size) {
            A = new int[size];
        }
        
        public void insert(int key) {
            maxHeapInsert(key);
        }
        
        public void printArray() {
            for (int i = 0; i < heapSize; i++) {
                System.out.printf("%d ", A[i]);
            }
            
            System.out.println();
        }
        
        public int extract() {
            return heapExtractMax();
        }
        
        private void maxHeapInsert(int key) {
            if (heapSize >= A.length) {
                int[] B = new int[A.length * 2];
                
                for (int i = 0; i < heapSize; i++) {
                    B[i] = A[i];
                }
                
                A = B;
            }
            
            heapSize += 1;
            A[heapSize - 1] = Integer.MIN_VALUE;
            heapIncreaseKey(heapSize - 1, key);
        }
        
        private void heapIncreaseKey(int i, int key) {
            if (key < A[i]) {
                return;
            }
            
            A[i] = key;
            
            while (i > 0 && A[parent(i)] < A[i]) {
                int tmp = A[parent(i)];
                
                A[parent(i)] = A[i];
                A[i] = tmp;
                i = parent(i);
            }
        }
        
        private void maxHeapify(int i) {
            int largest = i;
            
            if (left(i) < heapSize && A[left(i)] > A[largest]) {
                largest = left(i);
            }
            
            if (right(i) < heapSize && A[right(i)] > A[largest]) {
                largest = right(i);
            }
            
            if (largest != i) {
                int tmp = A[largest];
                
                A[largest] = A[i];
                A[i] = tmp;
                maxHeapify(largest);
            }
        }
        
        private int heapExtractMax() {
            if (heapSize < 1) {
                return Integer.MIN_VALUE;
            }
            
            int x = A[0];
            
            A[0] = A[heapSize - 1];
            heapSize -= 1;
            maxHeapify(0);
            
            return x;
        }
        
        private int parent(int i) {
            return (i - 1) / 2;
        }
        
        private int left(int i) {
            return 2 * i + 1;
        }
        
        private int right(int i) {
            return 2 * i + 2;
        }
    }
}
