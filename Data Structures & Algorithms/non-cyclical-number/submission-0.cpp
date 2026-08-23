#include <set>

class Solution {
public:
    bool isHappy(int n) {
        set<int> seen = {};
        while (seen.count(n) == 0) {
            if (n == 1) {
                return true;
            }
            seen.insert(n);
            long sumN = 0;
            while (n > 0) {
                int d = n % 10;
                sumN += d * d;
                n /= 10;
            }
            n = sumN;
        }
        return false;
    }
};
