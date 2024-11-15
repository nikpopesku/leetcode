#include <iostream>
#include <vector>
#include <algorithm>


using std::cout, std::endl;
//using std::max;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int rob(TreeNode* root) {
        return 4;
    }
};

int main() {
    auto s = Solution();
    auto a = new TreeNode(3, new TreeNode(2, nullptr, new TreeNode(3)), new TreeNode(3, nullptr, new TreeNode(1)));
    cout << s.rob(a) << endl;
}
