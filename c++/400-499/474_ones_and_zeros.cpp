#include <iostream>
#include <vector>
#include <algorithm>


using std::cout, std::endl, std::string, std::vector, std::count;
using std::max;

class Solution {
public:
    int findMaxForm(const vector<string> &strs, const int m, const int n) {
        vector dp(strs.size() + 1, vector(m + 1, vector(n + 1, 0)));
        int max_value = 0;

        for (size_t i = 0; i <= strs.size(); i++) {
            int zeros = 0;
            int ones = 0;
            for (const char s0 : strs[i]) {
                if (s0 == '1') ones++;
                if (s0 == '0') zeros++;
            }

            for (int j = m; j >= 0; j--) {
                for (int k = n; k >= 0; k--) {
                    if (j - zeros >= 0 and k - ones >= 0) {
                        int asdf = dp[i][j][k];
                        dp[i][j - zeros][k - ones] = max(dp[i][j][k] + 1, dp[i - 1][j][k]);
                        if (dp[i][j - zeros][k - ones] > max_value) {
                            max_value = dp[i][j - zeros][k - ones];
                        }
                    } else {
                        dp[i][j][k] = dp[i - 1][j][k];
                        if (dp[i][j][k] > max_value) {
                            max_value = dp[i][j][k];
                        }
                    }
                }
            }
        }

        return max_value;
    }
};

int main() {
    auto s = Solution();
    cout << s.findMaxForm({"10", "0001", "111001", "1", "0"}, 5, 3) << endl;
}
