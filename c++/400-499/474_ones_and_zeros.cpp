#include <iostream>
#include <vector>
#include <algorithm>


using std::cout, std::endl, std::string, std::vector, std::count;
using std::max;

class Solution {
public:
    int findMaxForm(const vector<string>& strs, int m, int n) {
        vector dp (strs.size()+1, vector (m+1, vector(n+1, 0)));

        for (size_t i = 0; i <= strs.size(); i++) {
            int zeros = std::count(strs[i].begin(), strs[i].end(), '0');
            int ones = std::count(strs[i].begin(), strs[i].end(), '1');
            if (m - zeros >= 0 and n - ones >= 0) {
                dp[i][m - zeros][n - ones] = max(dp[i][m][n] + 1, dp[i-1][m][n]);
                m -= zeros;
                n -= ones;
            } else {
                dp[i][m][n] = dp[i-1][m][n];
            }
            // for (int j=0; j <= m; j++) {
            //     for (int k =0; k <= n; k++) {
            //
            //     }
            // }
        }

        return 3;
    }
};

int main() {
    auto s = Solution();
    cout << s.findMaxForm({"10","0001","111001","1","0"}, 5, 3) << endl;
}
