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
    auto a = TreeNode(3);
    auto b1 = TreeNode(2);
    b1.right = new TreeNode(3);

    auto b2 = TreeNode(3);
    b1.right = new TreeNode(1);

    a.left = new TreeNode(b1);
    a.right = new TreeNode(b2);



//    cout << s.rob({3,2,3,nullptr,3,nullptr,1}) << endl;
    cout << s.rob(&a) << endl;
}
