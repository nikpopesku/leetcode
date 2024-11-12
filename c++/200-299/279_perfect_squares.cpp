#include <cmath>
#include <iostream>
#include <vector>
#include <climits>

class Solution {
public:
    int numSquares(int n) {
        std::vector dp (n, INT_MAX);
        dp[0] = 1;

        std::vector<int> squares {};

        for (int i = 1; i < std::sqrt(n); i++) {
            squares.push_back(i * i);
        }

        for (int i = 1; i < n; i++) {
            for (const auto sq: squares) {
                if (sq > n - i) {
                    break;
                }

                dp[i] = std::min(dp[i], dp[i-1] + 1);
            }
        }

        return dp[n-1];
    }
};


int main() {
    auto s = Solution();
    std::cout << s.numSquares(12) << std::endl;
}
