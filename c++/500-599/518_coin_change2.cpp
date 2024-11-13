#include <cmath>
#include <iostream>
#include <vector>

class Solution {
public:
    int change(const int amount, const std::vector<int>& coins) {
        std::vector dp(amount+1, 0);
        dp[0] = 1;

        for (int i = 1; i <= amount; i++) {
            for (auto& c: coins) {
                if (i - c >= 0) {
                    dp[i] += dp[i-c];
                }
            }
        }

        return dp[amount];
    }
};


int main() {
    auto s = Solution();
    std::cout << s.change(5, {1,2,5}) << std::endl;
}
