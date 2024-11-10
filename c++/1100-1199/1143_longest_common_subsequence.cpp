#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonSubsequence(const string& text1, const string& text2) {
        vector dp (text1.size()+1, vector<size_t>(text2.size()+1, 0));

        return calc(text1, text2);
    }
private:
    string calc(const string &s1, const string &s2) {
        static const string empty;
        if (s1.empty() or s2.empty()) return empty;

        if (s1[0] != s2[0]) {
            auto r1 = calc(s1.substr(1, s1.size() - 1), s2);
            auto r2 = calc(s1, s2.substr(1, s2.size() - 1));

            if (r1.size() > r2.size()) {
                return r1;
            }
        }

        return s1[0] + calc(s1.substr(1, s1.size() - 1), s2.substr(1, s2.size() - 1));
    }
};


int main() {
    auto s = Solution();
    cout << s.longestCommonSubsequence("abcde", "ace") << endl;
}
