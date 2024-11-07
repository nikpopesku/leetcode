#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    char findTheDifference(string s, string t) {
        unordered_map<char, int> map {};

        for (size_t i = 0; i < s.length(); i++) {
            if (map.find(s[i]) == map.end()) {
                map[s[i]] = 0;
            }

            map[s[i]]++;
        }

        for (size_t i = 0; i < t.length(); i++) {
            if (map.find(t[i]) != map.end()) {
                map[t[i]]--;
            }

            if (map[t[i]] == 0) {
                map.erase(t[i]);
            }
        }

        return map.begin()->first;
    }
};


int main() {
    auto s = Solution();
    cout << s.findTheDifference("abcd", "abcde") << endl;
}
