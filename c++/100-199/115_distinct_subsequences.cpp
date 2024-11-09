#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int numDistinct(const string &s, const string &t) {
        std::vector<std::vector<int>> dp;
        dp.resize(s.size() + 1, std::vector(t.size(), 0));
        dp[0][0] = 1;

        for (int i = 1; i <= s.size(); i++) {
            dp[i][0] = 1;
        }

        for (int j = 1; j < t.size(); j++) dp[0][j] = 1;

        for (size_t i = 1; i <= s.size(); i++) {
            for (size_t j = 1; j < t.size(); j++)
                dp[i][j] = dp[i - 1][j];
        }

        return dp[s.size()][t.size()-1];
    }
};


int main() {
    auto s = Solution();
    cout << s.numDistinct("rabbbit", "rabbit") << endl;
}
