#include <iostream>
#include <vector>
#include <algorithm>


using std::cout, std::endl;

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
        if (root = nullptr) return 0;
        auto grandson_left_left = nullptr;
        if (root.left) grandson_left_left = root.left.left;
        auto grandson_left_right = nullptr;
        if (root.left) grandson_left_right = root.left.right

        auto grandson_right_left = nullptr;
        if (root.right) grandson_right_left = root.right.left;
        auto grandson_right_right = nullptr;
        if (root.right) grandson_right_right = root.right.right

        return std::max(root.val + rob(grandson_left_left) + rob(grandson_left_right) + rob(grandson_right_left) + rob(grandson_right_right), root(root.left) + rob(root.right));
    }
};

int main() {
    auto s = Solution();
    auto a = new TreeNode(3, new TreeNode(2, nullptr, new TreeNode(3)), new TreeNode(3, nullptr, new TreeNode(1)));
    cout << s.rob(a) << endl;
}
