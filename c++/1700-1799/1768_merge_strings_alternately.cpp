#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    Solution () {};

    string mergeAlternately(string word1, string word2) {
        int i {0}, j{0};

        while (i < word1.length() and j < word2.length()) {
            if (i < word1.length()) {
                cout << word1[i];
                i++;
            }

            if (j < word2.length()) {
                cout << word2[j];
                j++;
            }
        }

    }
};


int main()
{


    auto s = Solution();
    s.mergeAlternately("abc", "pqr");
}
