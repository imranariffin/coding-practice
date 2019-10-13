public class Solution {
    public void wiggleSort(int[] nums) {
        Arrays.sort(nums);
        
        boolean flipFlop = true;
        
        // System.out.println(getPrint(nums));
        
        for (int i = 1; i < nums.length - 1; i++) {
            int swapIndex = getIndex(nums, i + 1, nums.length - 1, flipFlop);
            
            if (flipFlop) {
                if (nums[swapIndex] > nums[i]) {
                    swap(nums, i, swapIndex);
                }
            }
            else {
                if (nums[swapIndex] < nums[i]) {
                    swap(nums, i, swapIndex);
                }
            }
            
            // System.out.println(getPrint(nums));
            
            flipFlop = !flipFlop;
        }
    }
    
    private int getIndex(int[] nums, int s, int e, boolean type) {
        int indexSmall = 0;
        int valueSmall = Integer.MAX_VALUE;
        int indexBig = 0;
        int valueBig = Integer.MIN_VALUE;
        
        for (int i = s; i <= e; i++) {
            if (nums[i] > valueBig) {
                indexBig = i;
                valueBig = nums[i];
            }
            
            if (nums[i] < valueSmall) {
                indexSmall = i;
                valueSmall = nums[i];
            }
        }
        
        return type ? indexBig : indexSmall;
    }
    
    private void swap(int[] nums, int a, int b) {
        int aValue = nums[a];
        
        nums[a] = nums[b];
        nums[b] = aValue;
    }
    
    private String getPrint(int[] nums) {
        StringBuilder sb = new StringBuilder();
        
        for (int x : nums) {
            sb.append(x);
        }
        
        return sb.toString();
    }
}
