class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> vals = set(nums.begin(), nums.end());
        int result = 0;
        for (const int& num: nums) {
            if (vals.count(num) == 0) {
                continue;
            }

            int local = 1;
            vals.erase(num);
            
            // down
            int d = num - 1;
            while (vals.count(d) > 0) {
                local += 1;
                vals.erase(d);
                d -= 1;
            }

            // up
            int u = num + 1;
            while (vals.count(u) > 0) {
                local += 1;
                vals.erase(u);
                u += 1;
            }

            result = max(result, local);
        }

        return result;
    }
};
