#include <string>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonSubsequence(const string& text1, const string& text2) {
        return calc(text1, text2);
    }
private:
    string calc(const string &s1, const string &s2) {
        static const string empty;
        if (s1.empty() or s2.empty()) return empty;
        string key = to_string(s1.size()) + "_" + to_string(s2.size());
        if (dp.find(key) != dp.end()) return dp[key];

        if (s1[0] != s2[0]) {
            auto r1 = calc(s1.substr(1, s1.size() - 1), s2);

            if (const auto r2 = calc(s1, s2.substr(1, s2.size() - 1)); r1.size() > r2.size()) {
                return r1;
            }
        }

        dp[key] = s1[0] + calc(s1.substr(1, s1.size() - 1), s2.substr(1, s2.size() - 1));

        return dp[key];
    }

    unordered_map<string, string> dp {};
};


int main() {
    auto s = Solution();
    cout << s.longestCommonSubsequence("abcde", "ace") << endl;
}
