class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int res = 0;
        int n = nums.size();
        for (int i = 0; i < 32; i++) {
            int x = 0, y = 0;
            for (int num : nums) {
                x += (num >> i) & 1;
            }
            for (int j = 1; j < n; j++) {
                y += (j >> i) & 1;
            }
            if (x > y) {
                res |= 1 << i;
            }
        }
        return res;
    }
};
