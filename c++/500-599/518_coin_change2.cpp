#include <iostream>
#include <vector>

class Solution {
public:
    int change(const int amount, const std::vector<int>& coins) {
        std::vector dp (coins.size()+1, std::vector (amount+1, 0));

        for (int i = 0; i <= coins.size(); i++) {
            dp[i][0] = 1;
        }

        for (int i = coins.size(); i >= 0; i--) {
            for (int j = 0; j <= amount; j++) {
                if (coins[i] > amount) {
                    dp[i][j] = dp[i+1][j];
                } else {
                    dp[i][j] = dp[i+1][j] + dp[amount - coins[i]][j];
                }
            }
        }

        return dp[amount][coins.size()];
    }
};


int main() {
    auto s = Solution();
    std::cout << s.change(5, {1,2,5}) << std::endl;
}
