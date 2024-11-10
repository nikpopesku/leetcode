#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonSubsequence(string text1, string text2) {
        vector<size_t> dp (text1.size()+1, vector<size_t>(text2.size()+1, 0));
    }
private:
    string calc(string s1, string s2) {
        if (s1.empty() or s2.empty()) return '';


        if (s1[0] != s2[0]) {
            auto r1 = calc(s1.substr(1, s1.size() - 1), s2);
            auto r2 = calc(s1, s2.substr(1, s2.size() - 1));

            if (r1.size() > r2.size()) {
                return r1;
            }

            return r2;
        }
    }
};


int main() {
    auto s = Solution();
    cout << s.longestCommonSubsequence("abcde", "ace") << endl;
}
