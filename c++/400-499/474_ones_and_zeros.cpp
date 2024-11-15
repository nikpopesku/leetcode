#include <iostream>
#include <vector>

using std::vector;
using std::cout, std::endl, std::string;

class Solution {
public:
    int findMaxForm(const vector<string>& strs, int m, int n) {
        vector dp (strs.size()+1, vector (m+1, vector(n+1, 0)));

        return 3;
    }
};

int main() {
    auto s = Solution();
    cout << s.findMaxForm({"10","0001","111001","1","0"}, 5, 3) << endl;
}
