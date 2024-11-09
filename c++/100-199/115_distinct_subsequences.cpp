#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int numDistinct(const string &s, const string &t) {
        vector dp (s.size() + 1, 0);
        dp[0] = 1;

        for (int i = 1; i <= s.size(); i++) {
            for (int j = 0; j < t.size(); j++) {
                if (s[i - 1] == t[j]) {
                    dp[i] += dp[i - 1];
                }
            }
        }

        return dp[s.size()];
    }
};


int main() {
    auto s = Solution();
    cout << s.numDistinct("rabbbit", "rabbit") << endl;
}
