#include <string>
#include <iostream>
#include <vector>

class Solution {
public:
    int numSquares(int n) {
        return n + 1;
    }
};


int main() {
    auto s = Solution();
    std::cout << s.numSquares(12) << std::endl;
}
