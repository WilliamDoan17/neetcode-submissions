/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int computeDiameter(TreeNode *root, int *res) { 
        if (!root) return 0;
        int hleft = computeDiameter(root->left, res);
        int hright = computeDiameter(root->right, res);
        *res = max(*res, hleft + hright);
        return 1 + max(hleft, hright);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        if (!root) return 0;
        int res = 0;
        computeDiameter(root, &res);
        return res;
    }
};
