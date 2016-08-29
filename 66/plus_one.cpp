class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        return plusN(digits, 1);
    }
    
    vector<int> plusN(vector<int>& digits, int n) {
        vector<int> ret;
        
        int carry = n;
        for (int i=digits.size()-1; i>=0; i--) {
            ret.insert(ret.begin(), (digits[i] + carry)%10);
            if (carry!=0)
                carry = (digits[i] + 1)/10;
        }
        
        if (carry!=0) {
            ret.insert(ret.begin(), carry);
        }
        
        return ret;
    }
};